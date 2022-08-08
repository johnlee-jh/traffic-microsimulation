# Open source tools for traffic microsimulation creation, calibration and validation with Aimsun

This repository aims to provide open source tools to create traffic microsimulation of any city.

It has been created during a project with the objective to replicate Fremont San Jose neighborhood traffic with the traffic microsimulator software Aimsun.
This work is part of a larger body of research done by members of the Mobile sensing lab at UC Berkeley about modelling the impact of routing behaviors on road traffic.

## Structure

This repository contains three folders and one submodule.

The three folders contain files used to create, calibrate, and validate the Aimsun traffic microsimulation. 
A high-level overview of the strucutre is as below.

- `aimsun_scripts/`: Contains files that interact directly with Aimsun to create and execute the simulation.
- `calibration/`: Contains files that calibrate and/or analyze simulations after it has been run.
- `utils/`: Contains files that standardize dataclasses and filepaths throughout the repository.

The submodule contains example data for the city of Fremont to help users understand the structure and outputs of this repository as well as the traffic simulation.
- `fremont-public-data`: Contains files that contain processed data from public sources for the city of Fremont.

## Process

To create a new traffic microsimulation for a city, the user must first create Aimsun input data from raw data sources.

This premodeling step varies largely from city to city, and so users must create their own pipeline to convert raw data into Aimsun input data.
However, as long as the resultants of the premodeling step follows the dataclasses and filepaths specified in the table below, the data is compatible with the rest of our process.

| Aimsun Input Data Name | Dataclass | Filepath |
|---|---|---|
| Centroid Configuration | `utils.aimsun_input_utils.CentroidConfiguration` | Given by `utils.aimsun_folder_utils.centroid_connections_aimsun_input_file()` |
| Origin-Destination Demand Matrices | `utils.aimsun_input_utils.OriginDestinationMatrices` | Given by  `utils.aimsun_folder_utils.od_demand_aimsun_input_file()` |
| Master Control Plan | `utils.aimsun_input_utils.MasterControlPlan` | Given by  `utils.aimsun_folder_utils.master_control_plan_aimsun_input_file()` |
| Speed Limits and Capacities | `utils.aimsun_input_utils.SectionSpeedLimitsAndCapacities` | Given by  `utils.aimsun_folder_utils.speed_and_capacity_aimsun_input_file()` |
| Traffic Management Strategies | `utils.aimsun_input_utils.TrafficManagementStrategy` | Given by  `utils.aimsun_folder_utils.traffic_management_aimsun_input_file()` |
| Flow Detectors | `utils.aimsun_input_utils.AimsunFlowRealDataSet` | Given by  `utils.aimsun_input_utils.detector_flow_aimsun_input_file()` |

Once Aimsun input data is ready, the user should create a configuration file for the simulation by running Step 1 (Configure microsimulations) in `calibration/microsimulation_config_and_analysis.ipynb`.

Then, the user should execute Aimsun scripts to automatically load and run the simulation.
The process to do so is detailed in the README under `aimsun_scripts/`.

Once the simulation is complete and the output database is available, the user can further proceed with next steps in the analysis notebook at `calibration/microsimulation_config_and_analysis.ipynb`.

After this step, it is up to the user to assess the accuracy of the simulation according to real data sets and calibrate the simulation.

## Dependencies

Python dependencies are listed in requirements.txt.
Please run `pip3 install -r requirements.txt` to install all packages.

***

Last updated for Aimsun v22.0.1
