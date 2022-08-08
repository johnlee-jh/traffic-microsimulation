"""This script is used to create dynamic simulations that are used within
Aimsun. The script attempts to create scenarios and experiments from the
imported python AimsunScenario object. Then, each scenario creates an
experiment. All of the data from the Python AimsunScenario is loaded into
Aimsun this way.
"""

import aimsun_config_utils
from aimsun_folder_utils import (
    aimsun_macro_simulation_config_input_file,
    aimsun_micro_simulation_config_input_file,
    aimsun_output_directory_path
)
from aimsun_utils_functions import (
    create_macroscenarios,
    create_gk_scenario_and_experiment
)


MACRO_BASELINE = False
MICRO_BASELINE = False
CREATE_SENSITIVITY_SIMULATIONS = False
GENETIC_ALGORITHM_MICROSIMULATIONS = False


def create_q_date(year: int, month: int, day: int):
    """Generate a QDate object that corrseponds to a specific year and date.

    Args:
        year: Year of the scenario.
        month: Month of the scenario.
        day: Day of the scenario.
    Returns:
        QDate(year, month, day): QDate object of defined year, month, and day.
    """
    return QDate(year, month, day)


def create_trajectory_condition():
    """Generate a blank GKTrajectoryCondition.

    Returns:
        GKTrajectoryCondition(): Blank trajectory condiction.
    """
    return GKTrajectoryCondition()


if MACRO_BASELINE:
    print('Creating baseline macrosimulation...')
    aimsun_macro_simulation_file = aimsun_macro_simulation_config_input_file()
    print(f'Loading config from {aimsun_macro_simulation_file}...')
    aimsun_static_macroscenarios = (
        aimsun_config_utils.AimsunStaticMacroScenarios(
            aimsun_macro_simulation_file))
    print('Creating the scenarios...')
    create_macroscenarios(
        aimsun_static_macroscenarios, model, GKSystem.getSystem(),
        create_q_date, aimsun_output_directory_path())
    print('Done')
elif MICRO_BASELINE:
    print('Creating baseline microsimulation...')
    aimsun_micro_simulation_file = aimsun_micro_simulation_config_input_file()
    print(f'Loading config from {aimsun_micro_simulation_file}...')
    aimsun_microscenario = aimsun_config_utils.AimsunScenario(
        aimsun_micro_simulation_file)
    print('Creating the scenario...')
    create_gk_scenario_and_experiment(
        aimsun_microscenario, model, GKSystem.getSystem(),
        create_q_date, create_trajectory_condition,
        aimsun_output_directory_path())
    print('Done')
elif CREATE_SENSITIVITY_SIMULATIONS:
    print('Creating sensitivity analysis simulations...')
    with open(aimsun_sensitivity_analysis_unique_simulation_names_file(),
              "r", encoding="utf-8") as file:
        for unique_name in file.read().splitlines():
            print(f'Loading config from {unique_name}...')
            aimsun_microscenario = aimsun_config_utils.AimsunScenario(
                aimsun_micro_simulation_config_input_file(f"{unique_name}.pkl"))
            print('Creating the scenarios...')
            create_gk_scenario_and_experiment(
                aimsun_microscenario, model, GKSystem.getSystem(),
                create_q_date, create_trajectory_condition,
                aimsun_output_directory_path())
    print('Done')
elif GENETIC_ALGORITHM_MICROSIMULATIONS:
    for i in range(aimsun_config_utils.
                   GENETIC_ALGORITHM_NUM_INDIVIDUAL_PER_GENERATION):
        print(f'Creating individual {i} microsimulation...')
        aimsun_micro_simulation_file = (
            aimsun_micro_simulation_config_input_file(
                f'current_generation_individual_{i}.pkl'))
        print(f'Loading config from {aimsun_micro_simulation_file}...')
        aimsun_microscenario = aimsun_config_utils.AimsunScenario(
            aimsun_micro_simulation_file)
        print('Creating the scenario...')
        create_gk_scenario_and_experiment(
            aimsun_microscenario, model, GKSystem.getSystem(),
            create_q_date, create_trajectory_condition,
            aimsun_output_directory_path())
