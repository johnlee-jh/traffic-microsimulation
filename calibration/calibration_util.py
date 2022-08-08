"""Classes and methods to help with the od_demand_calibration notebook."""


import datetime
import os
from os import path
import pickle
import sys
from typing import Dict, List, Tuple
import warnings

import geopandas as gpd  # pylint: disable=import-error
from shapely.geometry import Point  # pylint: disable=import-error

module_path = os.path.abspath(os.path.join('..', 'Utils'))
if module_path not in sys.path:
    sys.path.append(module_path)
module_path = os.path.abspath(
    os.path.join('..', 'Traffic_data', 'Flow_and_speed_data'))
if module_path not in sys.path:
    sys.path.append(module_path)

from aimsun_input_utils import (  # pylint: disable=import-error, wrong-import-position
    AimsunFlowRealDataSet,
    CentroidConnection,
    ExternalId,
    OriginDestinationMatrices,
    VehicleTypeName,
)


class ExternalDemandData:
    """Data class for all External Demand Data from one external centroid to
    another external centroid.

    This data class is used to first hold StreetLight External demand data and
    later used to join Detector Flow Data with StreetLight data to perform
    external demand calibration.

    Attributes:
        origin_centroid_id: Origin centroid ID, in the form of 'ext_N' for
            external and 'local' for internal centroids.
        origin_detector_id: Origin from-detector ID that correspons to the
            centroid. Usually a six digit string, or 0 when 'local'.
        destination_centroid_id: Destination centroid ID, in the form of 'ext_N'
            for external and 'local' for internal centroids.
        destination_detector_id: Origin to-detector ID that correspons to the
            centroid. Usually a six digit string, or 0 when 'local'.
        streetlight_afternoon_flow: Afternoon flow from 14:00 to 19:45
            according to StreetLight data.
        from_detector_afternoon_flow: Afternoon flow from 14:00 to 19:45
            according to from-detector flow data.
        to_detector_afternoon_flow: Afternoon flow from 14:00 to 19:45
            according to to-detector flow data.
        from_demand_per_timestep: Demand per 15 minute intervals from 00:00 to
            23:45 according to from-detector flow data.
        to_demand_per_timestep: Demand per 15 minute intervals from 00:00 to
            23:45 according to to-detector flow data.
    """
    origin_centroid_id: ExternalId
    origin_detector_id: ExternalId
    destination_centroid_id: ExternalId
    destination_detector_id: ExternalId
    streetlight_afternoon_flow: float
    streetlight_demand_per_timestep: Dict[datetime.time, float]
    from_detector_afternoon_flow: float
    to_detector_afternoon_flow: float
    from_demand_per_timestep: Dict[datetime.time, float]
    to_demand_per_timestep: Dict[datetime.time, float]

    def __init__(self):
        self.origin_detector_id = None
        self.destination_detector_id = None
        self.from_detector_afternoon_flow = None
        self.to_detector_afternoon_flow = None
        self.from_demand_per_timestep = {}
        self.to_demand_per_timestep = {}

    def __str__(self):
        if (self.from_detector_afternoon_flow is None
                and self.to_detector_afternoon_flow is None):
            to_print = f"{self.origin_centroid_id} -> \
                {self.destination_centroid_id}, \
                Streetlight Afternoon demand = \
                {self.streetlight_afternoon_flow}"
            return to_print
        to_print = f"{self.origin_centroid_id} -> \
                {self.destination_centroid_id}, \
                Streetlight Afternoon demand = \
                {self.streetlight_afternoon_flow} \n \
                From-Detector Afternoon demand = \
                {self.from_detector_afternoon_flow} \n \
                To-Detector Afternoon demand = \
                {self.to_detector_afternoon_flow}"
        return to_print

    def __eq__(self, other):
        return str(self) == str(other)


class ExternalDemandProfile:
    """Data class for External Demand Profile (StreetLight data merged with
    detector flow data).

    This class is used within the Calibration notebook to calibrate external
    demand.

    Attributes:
        ext_demand_matrix: List of ExternalDemandData for every external to
            external centroid combination.
    """
    ext_demand_matrix: List[ExternalDemandData]

    def __init__(self, filepath: str = ""):
        self.ext_demand_matrix = []
        if filepath != "":
            self.__import_from_file(filepath)

    def export_to_file(self, filepath: str):
        """Export ExternalDemandProfile to file by serializing
        ext_demand_matrix.

        Raises exception if the ext_demand_matrix is empty. Warns the user
        if a file already exists at filepath and overwrites it.
        """
        # Check if ext_demand_matrix is empty.
        if len(self.ext_demand_matrix) == 0:
            raise Exception(
                'ExternalDemandProfile has no data. Export aborted.')
        # Check if file exists at given filepath.
        if path.exists(filepath):
            warnings.warn('File already exists at filepath. Overwriting file.')
        # Serialize ext_demand_matrix and write to filepath.
        with open(filepath, 'wb') as file:
            pickle.dump(self.ext_demand_matrix, file)

    def __import_from_file(self, filepath: str):
        """Import ExternalDemandProfile from file by deserializing
        ext_demand_matrix.

        Raises exception if the given file does not match the data type of
        ext_demand_matrix (List[ExternalDemandData]).
        """
        # Deserialize ext_demand_matrix from filepath.
        with open(filepath, 'rb') as file:
            imported_data = pickle.load(file)
        # Check if imported data matches data type of ext_demand_matrix.
        if (isinstance(imported_data, list)
                and isinstance(imported_data[0], ExternalDemandData)):
            self.ext_demand_matrix = imported_data
        else:
            raise Exception("File has incorrect data type. Import aborted.")

    def __str__(self):
        to_print = ''
        for ext_demand_data in self.ext_demand_matrix:
            to_print += str(ext_demand_data) + '\n'
        return to_print

    def __eq__(self, other) -> bool:
        return str(self) == str(other)
