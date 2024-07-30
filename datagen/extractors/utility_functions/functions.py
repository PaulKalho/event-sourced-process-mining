import os
import json
import pm4py
import pandas as pd
import requests

from util.environment import ENV


def write_to_file(results: dict, output_file: str) -> None:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)


def write_xes_to_file(event_log, output_file: str) -> None:
    """
    Wrapper function for pm4pys write xes to file, as folder may
    have to be created
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    pm4py.write_xes(event_log, output_file)


def format_df_to_eventlog(df: pd.DataFrame) -> pd.DataFrame:
    """
    Wrapper function for pm4py's format_dataframe function
    """
    return pm4py.format_dataframe(
        df,
        case_id="CaseID",
        activity_key="Activity",
        timestamp_key="Timestamp"
    )


def fetch_projection_results(projection_name: str) -> dict:
    url = f"http://{ENV.EVENTSTORE_HOST}:{
        ENV.EVENTSTORE_PORT}/projection/{projection_name}/result"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
