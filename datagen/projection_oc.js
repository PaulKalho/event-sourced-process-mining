fromAll()
    .when({
        $init: function() {
            return {
                events: {},
                objects: {},
            };
        },
        $any: function(state, event) {
            if (event.eventType === "PATIENT_CREATED_v1") {
                var patientStreamId = event.streamId;

                // Add the patient stream as object
                state.objects[patientStreamId] = {
                    type: 'patient',
                    id: patientStreamId,
                    human_readable_identifier: event.data.human_readable_identifier,
                };

                // Add the event itself to the events
                state.events[event.eventId] = {
                    activity: event.eventType,
                    timestamp: event.metadata.timestamp,
                    related_objects: [
                        patientStreamId
                    ]
                }
            } else if (event.eventType === "TASK_CREATED_v1") {
                var taskStreamId = event.streamId;

                // Add the task stream as object
                state.objects[taskStreamId] = {
                    type: 'task',
                    id: taskStreamId,
                    name: event.data.name
                }

                // Add the task event itself to the events
                // The task is also connected to the patient object
                state.events[event.eventId] = {
                    activity: event.eventType,
                    timestamp: event.metadata.timestamp,
                    related_objects: [
                        taskStreamId,
                        "patient-" + event.data.patient_id
                    ]
                }
            } else if (event.eventType === "PROPERTY_CREATED_v1") {
                var propertyStreamId = event.streamId;

                state.object[propertyStreamId] = {
                    type: 'property',
                    id: propertyStreamId,
                    name: event.data.name
                }

                state.events[event.eventId] = {
                    activity: event.eventType,
                    timestamp: event.metadata.timestamp,
                    related_objects: [
                        propertyStreamId
                    ]
                }
            } else if (event.eventType === "PROPERTY_VALUE_CREATED_v1") {
                var propertyValueStreamId = event.streamId;

                state.object[propertyValueStreamId] = {
                    type: 'property-value',
                    id: propertyValueStreamId,
                    name: event.data.value
                }

                state.events[event.eventId] = {
                    activity: event.eventType,
                    timestamp: event.metadata.timestamp,
                    related_objects: [
                        "property-" + event.data.property_id,
                        // TODO: we assume all property values are linked to a patient, in reality this will not be the case
                        "patient-" + event.data.subject_id
                    ]
                }
            } else {
                // All other events, link them to its stream
                state.events[event.eventId] = {
                    activity: event.eventType,
                    timestamp: event.metadata.timestamp,
                    related_objects: [
                        event.streamId
                    ]
                }

            }
        }
    });
