import connexion
import six

from swagger_server.models.data_utility import DataUtility  # noqa: E501
from swagger_server.models.refinement_request import RefinementRequest  # noqa: E501
from swagger_server import util

import DQWeighter
import json
import pandas as pd
import os

def refinement(datautility):  # noqa: E501
    """recalculate the data utility based on the application

    By passing the DataUtility values and the application it returns new DataUtility values depending on the application # noqa: E501

    :param datautility: data utility values
    :type datautility: dict | bytes

    :rtype: DataUtility
    """


    print(datautility)

    application=datautility['application']
    dimensions=datautility['datautility']

    results=DQWeighter.DQWeighter(dimensions,application)



    return results

