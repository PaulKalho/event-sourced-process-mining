This repository contains all scripts I used for my bachelor thesis.

It contains scripts that can be used to synthetically create event-sourced data by utilizing the [helpwave/services](https://github.com/helpwave/services/) architecture.
This generated data will then be used for process mining.

### Prerequisites

1. Install the requirements
```sh
pip install -r requirements.txt
```

### discovery

Within the discovery folder you can find an exemplary event log and a python script that uses the inducitve_miner to discover the process from the underlying event log.

Navigate into the discovery folder to see the instructions.

### datagen

Within the datagen folder you can find the data simulator scripts, I used to create synthetic data on the helpwave/services infrastructure. Moreover, it also contains the extrator scripts that do data reshaping and process discovery.

Navigate into the datagen folder to find the instructions.
