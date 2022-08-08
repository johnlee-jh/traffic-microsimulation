"""Executes Aimsun simulation scenario."""

from typing import List
from aimsun_utils_functions import run_experiments

import aimsun_config_utils
import aimsun_input_utils
from aimsun_folder_utils import (
    aimsun_macro_simulation_config_input_file,
    aimsun_micro_simulation_config_input_file
)


RUN_MACRO_BASELINE = False
RUN_MICRO_BASELINE = False
RUN_SENSITIVITY_ANALYSIS = False
RUN_GENETIC_ALGORITHM_MICROSIMULATIONS = False

LIST_EXPERIMENT_EXTERNAL_ID: List[aimsun_input_utils.ExternalId] = []

if RUN_MACRO_BASELINE:
    LIST_EXPERIMENT_EXTERNAL_ID = [
        scenario.experiment.external_id for scenario
        in aimsun_config_utils.AimsunStaticMacroScenarios(
            aimsun_macro_simulation_config_input_file(
            )).aimsun_static_macroscenarios
    ]
elif RUN_MICRO_BASELINE:
    LIST_EXPERIMENT_EXTERNAL_ID = [
        aimsun_config_utils.AimsunScenario(
            aimsun_micro_simulation_config_input_file(
            )).experiment.external_id
    ]
elif RUN_SENSITIVITY_ANALYSIS:
    with open(aimsun_sensitivity_analysis_unique_simulation_names_file(),
              "r", encoding='utf-8') as file:
        LIST_EXPERIMENT_EXTERNAL_ID = file.read().splitlines()
elif RUN_GENETIC_ALGORITHM_MICROSIMULATIONS:
    for i in range(aimsun_config_utils.
                   GENETIC_ALGORITHM_NUM_INDIVIDUAL_PER_GENERATION):
        LIST_EXPERIMENT_EXTERNAL_ID.append(f'current_generation_individual_{i}')

run_experiments(
    LIST_EXPERIMENT_EXTERNAL_ID, model, GKSystem.getSystem())
