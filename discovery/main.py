import pm4py

if __name__ == "__main__":
    log = pm4py.read_xes('log.xes')

    net, initial, final = pm4py.discover_petri_net_inductive(log)
    
    bpmn_graph = pm4py.convert_to_bpmn(net, initial, final)
    pm4py.view_bpmn(bpmn_graph)
