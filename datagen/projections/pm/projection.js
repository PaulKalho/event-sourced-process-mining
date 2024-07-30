// This javscript snippet can be used to create a projection on the EventstoreDB UI

fromAll()
    .when({
        $init: function() {
            return {
                patients: {}
            };
        },
        $any: function(state, event) {
            var patientId = event.data.patient_id;
            var streamId = event.streamId;

            if (patientId) {
                // Add the event to the patient's events
                state.patients[patientId].events.push({
                    type: event.eventType,
                    data: event.data,
                    timestamp: event.metadata.timestamp
                });

                // Add the stream to the associated_streams if it's not already there
                if (!state.patients[patientId].associated_streams.includes(streamId)) {
                    state.patients[patientId].associated_streams.push(streamId);
                }

            } else {
                if (event.eventType === "PATIENT_CREATED_v1") {
                    state.patients[event.data.id] = {
                        events: [],
                        associated_streams: [],
                        stream_id: streamId,
                    };
                }

                for (var pid in state.patients) {
                    if (state.patients[pid].associated_streams.includes(streamId) || state.patients[pid].stream_id === streamId) {
                        // Add the event to the patient's events
                        state.patients[pid].events.push({
                            type: event.eventType,
                            data: event.data,
                            timestamp: event.metadata.timestamp
                        });

                        break;
                    }
                }
            }

            return state;
        }
    })
    .outputState();
