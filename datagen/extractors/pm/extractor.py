import requests
import pandas as pd
import pm4py

from util.environment import ENV
from extractors.utility_functions.functions import write_xes_to_file, \
    write_to_file, format_df_to_eventlog, fetch_projection_results


def convert_to_dataframe(results: dict) -> pd.DataFrame:
    rows = []
    for patient_id, patient_data in result["patients"].items():
        for event in patient_data["events"]:
            row = {
                "CaseID": patient_id,
                "Activity": event["type"],
                "Timestamp": event["timestamp"]
            }
            row.update(event["data"])
            rows.append(row)

    df = pd.DataFrame(rows)
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], format="%Y-%m-%dT%H:%M:%S.%fZ", errors="coerce")

    return df


def squash_patterns(df: pd.DataFrame, pattern: list,
                    new_activity_name: str) -> pd.DataFrame:
    pattern_length = len(pattern)
    new_rows = []
    i = 0

    while i < len(df):
        pattern_fits = i < len(df) - pattern_length
        pattern_matches = all(
            df.iloc[i + j]["Activity"] == pattern[j]
            for j in range(pattern_length)
        )

        if pattern_fits and pattern_matches:
            # pattern detected
            new_row = df.iloc[i].copy()
            new_row["Activity"] = new_activity_name
            new_rows.append(new_row)
            i += pattern_length
        else:
            new_rows.append(df.iloc[i])
            i += 1

    return pd.DataFrame(new_rows)


def change_task_activity(data: pd.DataFrame, old_activity_key) -> pd.DataFrame:
    new_rows = []
    for index, row in data.iterrows():
        new_row = row.copy()
        if new_row[old_activity_key] == "task":
            new_row[old_activity_key] = row["name"]
        new_rows.append(new_row)
    return pd.DataFrame(new_rows)


def change_note_activity(data: pd.DataFrame, old_activity_key) -> pd.DataFrame:
    new_rows = []
    for index, row in data.iterrows():
        new_row = row.copy()
        if new_row[old_activity_key] == "NOTES_UPDATED_v1":
            new_row[old_activity_key] = row["notes"]
        new_rows.append(new_row)
    return pd.DataFrame(new_rows)


def reshape_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function reshapes the data
    1. Its squashes the task events
    2. Its suqashes the patient eventis
    3. It changes the activities to the corresponding attributes
    4. Filters out leftover technical events
    """
    task_status_squashed = squash_patterns(
        df,
        ["TASK_CREATED_v1", "TASK_DESCRIPTION_UPDATED_v1",
         "TASK_PUBLISHED_v1", "TASK_STATUS_UPDATED_v1"],
        "task"
    )
    task_squashed = squash_patterns(
        task_status_squashed,
        ["TASK_CREATED_v1", "TASK_DESCRIPTION_UPDATED_v1",
         "TASK_PUBLISHED_v1"],
        "task"
    )
    patient_squashed = squash_patterns(
        task_squashed,
        ["PATIENT_CREATED_v1", "BED_ASSIGNED_v1"],
        "Patient admitted"
    )

    task_activities = change_task_activity(patient_squashed, "Activity")
    note_activities = change_note_activity(task_activities, "Activity")

    # filter left over task_status_updated events
    return note_activities[note_activities["Activity"]
                           != "TASK_STATUS_UPDATED_v1"]


def discover_and_show(event_log) -> None:
    heu_net = pm4py.discover_heuristics_net(event_log)
    pm4py.view_heuristics_net(heu_net)


if __name__ == "__main__":
    try:
        result = fetch_projection_results(ENV.PROJECTION_NAME)
        write_to_file(
            result, f"{ENV.PROJECTIONS_OUTPUT_DIR}/pm/projection_result.json")

        df = convert_to_dataframe(result)
        formatted_df_technical = format_df_to_eventlog(df)

        event_log_technical = pm4py.convert_to_event_log(
            formatted_df_technical)
        write_xes_to_file(event_log_technical, f"{
            ENV.EVENT_LOG_OUTPUT_DIR}/pm/event_log_technical.xes")

        discover_and_show(event_log_technical)

        ###

        processed_data = reshape_data(formatted_df_technical)
        formatted_df_enhanced = format_df_to_eventlog(processed_data)

        event_log_shaped = pm4py.convert_to_event_log(formatted_df_enhanced)
        write_xes_to_file(event_log_shaped, f"{
            ENV.EVENT_LOG_OUTPUT_DIR}/pm/event_log_shaped.xes")

        discover_and_show(event_log_shaped)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching one-time projection result: {e}")
