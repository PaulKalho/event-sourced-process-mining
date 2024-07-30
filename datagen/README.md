### How to use

> [!IMPORTANT]
> [helpwave/services](https://github.com/helpwave/services/) has to be set up & running.
> Instructions inside the helpwave/services repository. 

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









