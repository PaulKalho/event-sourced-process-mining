import requests
import json
import pm4py

from util.environment import ENV

def write_to_file(result: dict, output_file: str) -> None:
    data_str = json.dumps(result, indent=4)
    print(data_str[0:15])
    with open(output_file, 'w') as f:
        f.write(data_str)   

def fetch_projection_results(projection_name: str) -> dict:
    url = f"http://{ENV.EVENTSTORE_HOST}:{ENV.EVENTSTORE_PORT}/projection/{projection_name}/result"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

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
            **{k: v for k,v in obj.items() if k not in ["type", "id"]},
            "ocel:ovmap": {}
        }
    
    return jsonocel

if __name__ == "__main__":
    try:
        data = fetch_projection_results(ENV.OC_PROJECTION_NAME)
        write_to_file(data, "oc_projection_result.json")

        json_ocel = convert_to_jsonocel(data)
        write_to_file(json_ocel, "ocel.jsonocel")

        ## technical mining
        ocel = pm4py.read_ocel("ocel.jsonocel")
        model = pm4py.discover_oc_petri_net(ocel)
        pm4py.view_ocpn(model, format="png")
        
        ## fetch enriched & mine
        data_enr = fetch_projection_results(ENV.OC_ENHANCED_PROJECTION_NAME)
        write_to_file(data, "oc_enhanced_results.json")

        json_enr_ocel = convert_to_jsonocel(data_enr)
        write_to_file(json_enr_ocel, "ocel_enr.jsonocel")

        enr_ocel = pm4py.read_ocel("ocel_enr.jsonocel")
        enr_model = pm4py.discover_oc_petri_net(enr_ocel)
        pm4py.view_ocpn(enr_model, format="png")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching one-time projection result:{e}")

