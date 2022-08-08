# Open source tools for traffic microsimulation creation, calibration and validation with Aimsun

This repository aims to provide open source tools to create traffic microsimulation of any city.

It has been created during a project with the objective to replicate Fremont San Jose neighborhood traffic with the traffic microsimulator software Aimsun.
This work is part of a larger body of research done by members of the Mobile sensing lab at UC Berkeley about modelling the impact of routing behaviors on road traffic.

## Structure

The repo contains four folders. A high-level over view of the strucutre is below, but please refer to the documentation inside each folder for details.

1. `aimsun_scripts`: Python scripts to be used when loading data and running simulations within Aimsun.
2. `calibration`: Aimsun ...
3. `utils`: Dataclasses and data folder path functions used throughout the repository.
4. `fremont-public-data`: Example data folder for the city of Fremont to aid understanding of the repository.

## Process

To create your own traffic microsimulation, you must first premodel the data such that the Aimsun input data in the table below exists, is of the specified dataclass, and is located in the specified filepath. 

The premodeling process varies largely between city to city, and so the user must create their own pipeline to process raw data into the format specified in the table below.

However, an example premodeling output is provided for the city of Fremont at `fremont-public-data/` to help understand premodeling goals or if you want to experiment with steps after premodeling.

| Data Name | Object Dataclass | Filepath |
|---|---|---|
| Centroid Configuration | `aimsun_input_utils.CentroidConfiguration` | Given by `aimsun_folder_utils.centroid_connections_aimsun_input_file()` |
| Origin-Destination Demand Matrices | `aimsun_input_utils.OriginDestinationMatrices` | Given by  `aimsun_folder_utils.od_demand_aimsun_input_file()` |
| Master Control Plan | `aimsun_input_utils.MasterControlPlan` | Given by  `aimsun_folder_utils.master_control_plan_aimsun_input_file()` |
| Speed Limits and Capacities | `aimsun_input_utils.SectionSpeedLimitsAndCapacities` | Given by  `aimsun_folder_utils.speed_and_capacity_aimsun_input_file()` |
| Traffic Management Strategies | `aimsun_input_utils.TrafficManagementStrategy` | Given by  `aimsun_folder_utils.traffic_management_aimsun_input_file()` |
| Flow Detectors | `aimsun_input_utils.AimsunFlowRealDataSet` | Given by  `aimsun_input_utils.detector_flow_aimsun_input_file()` |

Once premodeling data is ready, the user should create configuration files for the simulation by running Step 1 (Configure microsimulations) in `calibration/microsimulation_config_and_analysis.ipynb`.

Then, with the config ready, the user should execute the Aimsun simulation scripts to automatically load and run the simulation in Aimsun. The process to do so is detailed in the documentation under `aimsun_scripts/`.

After the simulation is run and output databases are available, the user can further proceed with `calibration/microsimulation_config_and_analysis.ipynb` to assess the accuracy of the simulation according to validation data and calibrate the simulation.

## Dependencies

Python dependencies are listed in requirements.txt.
Please run `pip3 install -r requirements.txt` to install all packages.

**Last updated: August 7th, 2022 for Aimsun v22.0.1**
