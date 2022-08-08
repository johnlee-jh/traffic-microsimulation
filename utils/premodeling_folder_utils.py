"""TODO: Docstring."""

from os import path
import metadata_settings


__YEAR_OF_SIMULATION = metadata_settings.get_simulation_year()
__DATA_FOLDER_PATH = metadata_settings.get_data_folder_path()


# Premodel Data
__PREMODELING_DATA_PATH = path.join(__DATA_FOLDER_PATH, 'premodel_data')
# - Demand
__DEMAND_DATA_PATH = path.join(__PREMODELING_DATA_PATH, 'demand')
# - External Centroids
__EXTERNAL_CENTROIDS_DATA_PATH = path.join(
    __PREMODELING_DATA_PATH, 'external_centroids')


def external_centroids_file() -> str:
    """Returns the external centroids shapefile location."""
    return path.join(
        __EXTERNAL_CENTROIDS_DATA_PATH, 'external_centroids.shp')


def external_demand_file() -> str:
    """Returns the external demand profile file location."""
    return path.join(
        __DEMAND_DATA_PATH, f'external_demand_{__YEAR_OF_SIMULATION}.pkl')


def od_demand_raw_file() -> str:
    """Returns the raw (uncalibrated) OD demand file location."""
    return path.join(
        __DEMAND_DATA_PATH, f'od_demand_raw_{__YEAR_OF_SIMULATION}.pkl')
