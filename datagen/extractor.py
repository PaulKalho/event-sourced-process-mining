import requests
import json
import time
import pandas as pd

import pm4py

from pm4py import convert_to_event_log, format_dataframe, write_xes
from pm4py.algo.discovery.heuristics.algorithm import apply as heuristics
from pm4py.visualization.petri_net import visualizer

from util.environment import ENV

def fetch_projection_results() -> dict:
    url = f"http://{ENV.EVENTSTORE_HOST}:{ENV.EVENTSTORE_PORT}/projection/{ENV.PROJECTION_NAME}/result"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def write_to_file(results: dict, output_file: str) -> None:
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

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
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%Y-%m-%dT%H:%M:%S.%fZ", errors="coerce")
    
    return df

def squash_patterns(df: pd.DataFrame, pattern: list, new_activity_name: str) -> pd.DataFrame:
    pattern_length = len(pattern)
    new_rows = []
    
    i = 0
    while i < len(df):
        if i < len(df) - pattern_length and all(df.iloc[i + j]["Activity"] == pattern[j] for j in range(pattern_length)):
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

if __name__ == "__main__":
    try:
        result = fetch_projection_results()
        write_to_file(result, "output.json")
        
        df = convert_to_dataframe(result)
        formatted_df = format_dataframe(df, case_id="CaseID", activity_key="Activity", timestamp_key="Timestamp" )
        
        event_log_technical = convert_to_event_log(formatted_df)
        write_xes(event_log_technical, 'event_log_technical.xes')

        # -- Heuristics
        # heu_net_technical = pm4py.discover_heuristics_net(event_log_technical)
        # pm4py.view_heuristics_net(heu_net_technical)
        # --

        # -- Inductive
        # technical_tree = pm4py.discover_process_tree_inductive(event_log_technical)
        # pm4py.view_process_tree(technical_tree)
        # net, initial_marking, final_marking = pm4py.convert_to_petri_net(tree)
        # pm4py.vis.view_petri_net(net)
        # --

        ### data reshaping ###
        task_status_squashed = squash_patterns(df, ["TASK_CREATED_v1", "TASK_DESCRIPTION_UPDATED_v1", "TASK_PUBLISHED_v1", "TASK_STATUS_UPDATED_v1"], "task")
        task_squashed = squash_patterns(task_status_squashed, ["TASK_CREATED_v1", "TASK_DESCRIPTION_UPDATED_v1", "TASK_PUBLISHED_v1"], "task")
        patient_squashed = squash_patterns(task_squashed, ["PATIENT_CREATED_v1", "BED_ASSIGNED_v1"], "Patient admitted")
        task_activities = change_task_activity(patient_squashed, "Activity")
        note_activities = change_note_activity(task_activities, "Activity")
        
        # remove the rest of the status updated
        final = note_activities[note_activities["Activity"] != "TASK_STATUS_UPDATED_v1"]
        test = format_dataframe(final, case_id='CaseID', activity_key="Activity", timestamp_key="Timestamp")
         
        event_log_shaped = convert_to_event_log(final)
        write_xes(event_log_shaped, 'event_log_shaped.xes')
        
        """ Inductive
        tree = pm4py.discover_process_tree_inductive(event_log_shaped)
        net, initial_marking, final_marking = pm4py.convert_to_petri_net(tree)
        pm4py.vis.view_petri_net(net)
        """

        heu_net = pm4py.discover_heuristics_net(event_log_shaped)
        pm4py.view_heuristics_net(heu_net)
        pm4py.vis.view_petri_net(net, format="pdf")        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching one-time projection result: {e}")
   



