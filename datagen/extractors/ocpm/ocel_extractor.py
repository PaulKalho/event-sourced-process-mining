import requests
import pm4py

from util.environment import ENV
from extractors.utility_functions.functions import fetch_projection_results, \
    write_to_file


def convert_to_jsonocel(data: dict) -> dict:
    jsonocel = {
        "ocel:global-event": {
            "ocel:activity": "__INVALID__"
        },
        "ocel:global-object": {
            "ocel:type": "__INVALID__"
        },
        "ocel:global-log": {
            "ocel:attribute-name": ["activity", "timestamp", "related_objects"],
            "ocel:object-types": list(set(obj["type"] for obj in data["objects"].values())),
            "ocel:version": "1.0"
        },
        "ocel:events": {},
        "ocel:objects": {}
    }

    for event_id, event in data["events"].items():
        jsonocel["ocel:events"][event_id] = {
            "ocel:activity": event["activity"],
            "ocel:timestamp": event["timestamp"],
            "ocel:omap": event["related_objects"],
            "ocel:vmap": {}
        }
    for obj_id, obj in data["objects"].items():
        jsonocel["ocel:objects"][obj_id] = {
            "ocel:type": obj["type"],
            **{k: v for k, v in obj.items() if k not in ["type", "id"]},
            "ocel:ovmap": {}
        }

    return jsonocel


if __name__ == "__main__":
    try:
        data = fetch_projection_results(ENV.OC_PROJECTION_NAME)
        write_to_file(
            data,
            f"{ENV.PROJECTIONS_OUTPUT_DIR}/ocpm/oc_projection_result.json"
        )

        json_ocel = convert_to_jsonocel(data)
        write_to_file(
            json_ocel, f"{ENV.EVENT_LOG_OUTPUT_DIR}/ocpm/ocel.jsonocel")

        # technical mining
        ocel = pm4py.read_ocel(
            f"{ENV.EVENT_LOG_OUTPUT_DIR}/ocpm/ocel.jsonocel")
        model = pm4py.discover_oc_petri_net(ocel)
        pm4py.view_ocpn(model, format="png")

        # fetch enriched & mine
        data_enr = fetch_projection_results(ENV.OC_ENHANCED_PROJECTION_NAME)
        write_to_file(
            data, f"{ENV.PROJECTIONS_OUTPUT_DIR}/ocpm/oc_enhanced_results.json")

        json_enr_ocel = convert_to_jsonocel(data_enr)
        write_to_file(json_enr_ocel, f"{
                      ENV.EVENT_LOG_OUTPUT_DIR}/ocpm/ocel_enr.jsonocel")

        enr_ocel = pm4py.read_ocel(
            f"{ENV.EVENT_LOG_OUTPUT_DIR}/ocpm/ocel_enr.jsonocel")
        enr_model = pm4py.discover_oc_petri_net(enr_ocel)
        pm4py.view_ocpn(enr_model)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching one-time projection result:{e}")
