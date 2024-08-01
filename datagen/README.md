### How to use

> [!IMPORTANT]
> [helpwave/services](https://github.com/helpwave/services/tree/issue/703-task-missing-endpoints) has to be set up & running.
> Instructions inside the helpwave/services repository. 

> [!IMPORTANT]
> Please ensure you have the correct version of the helpwave/services repository checked out to avoid compatibility issues and to get the same results as shown in the thesis.
> 
> Branch ```issue/703-task-missing-endpoints```
> 
> Commit Hash ```f949bac``` 

After the services and [EventstoreDB](https://www.eventstore.com/eventstoredb) is running,
you can start the simulator scripts.

## Scripts

> [!NOTE]
> Both simulator scripts should be run on an empty event-store to get the same results as in the thesis.

### Process Mining

1. Run the simulartor_pm.py

    ```sh
    python -m simulator_pm
    ```

    This can take a few minutes. The script will exit when finished.

2. Extract the data and display the process models

    Run:
    ```sh
    python extractors.pm.extractor 
    ```

### Object Centric Process Mining

1. Run the simulator_ocpm.py

    ```sh
    python -m simulator_ocpm
    ```

    This can take a few minutes. The script will exit when finished.

2. Extract the data and display the process models

    Run:
    ```sh
    python extractors.ocpm.ocel_extractor
    ```

## Data

The eventlogs can be found under:

```
output/event_logs/{ocpm/pm}/
```

The projections can be found under:

```
output/projections/{ocpm/pm}/
```

## Configurations

The default configurations can be found here:

| NAME                              | DEFAULT VALUE             | DESCRIPTION                               |
| ----------------------------------| --------------------------| ------------------------------------------|
| SERVICES_HOST                     | localhost                 | helpwave/services host                    |
| TASKS_PORT                        | 3004                      | Port of the tasks service                 |
| PROPERTY_PORT                     | 3005                      | Port of the property service              |
| EVENTSTORE_HOST                   | localhost                 | EventstoreDB host                         |
| PROJECTION_NAME                   | getAllEventsByPatientWithPatient | Name of the created projection for the normal process mining extractor script |
| OC_PROJECTION_NAME                | getObjectCentricEventLog  | Name of the created projection for the object centric process mining extractor script |
| OC_ENHANCED_PROJECTION_NAME       | getObjectCentricEventLogEnhanced   | Name of the created projection with enhanced activities for the object centric process mining extractor script |
| PROJECTIONS_OUTPUT_DIR            | output/projections        | Directory where the projection results will be saved |
| EVENT_LOG_OUTPUT_DIR              | output/event_logs         | Directory where the created event logs will be saved |
| LOG_LEVEL        | DEBUG                        | Log level      |

To configure these env variables, create a .env file inside this directory and define the variables.

For example:

```
TASKS_PORT=3069
PROPERTY_PORT=3042
```







