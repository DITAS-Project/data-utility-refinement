# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataUtility(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, url: str=None, accuracy: float=None, consistency: float=None, completeness: float=None, timeliness: float=None):  # noqa: E501
        """DataUtility - a model defined in Swagger

        :param url: The url of this DataUtility.  # noqa: E501
        :type url: str
        :param accuracy: The accuracy of this DataUtility.  # noqa: E501
        :type accuracy: float
        :param consistency: The consistency of this DataUtility.  # noqa: E501
        :type consistency: float
        :param completeness: The completeness of this DataUtility.  # noqa: E501
        :type completeness: float
        :param timeliness: The timeliness of this DataUtility.  # noqa: E501
        :type timeliness: float
        """
        self.swagger_types = {
            'url': str,
            'accuracy': float,
            'consistency': float,
            'completeness': float,
            'timeliness': float
        }

        self.attribute_map = {
            'url': 'URL',
            'accuracy': 'accuracy',
            'consistency': 'consistency',
            'completeness': 'completeness',
            'timeliness': 'timeliness'
        }

        self._url = url
        self._accuracy = accuracy
        self._consistency = consistency
        self._completeness = completeness
        self._timeliness = timeliness

    @classmethod
    def from_dict(cls, dikt) -> 'DataUtility':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataUtility of this DataUtility.  # noqa: E501
        :rtype: DataUtility
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this DataUtility.


        :return: The url of this DataUtility.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this DataUtility.


        :param url: The url of this DataUtility.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def accuracy(self) -> float:
        """Gets the accuracy of this DataUtility.


        :return: The accuracy of this DataUtility.
        :rtype: float
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy: float):
        """Sets the accuracy of this DataUtility.


        :param accuracy: The accuracy of this DataUtility.
        :type accuracy: float
        """
        if accuracy is None:
            raise ValueError("Invalid value for `accuracy`, must not be `None`")  # noqa: E501

        self._accuracy = accuracy

    @property
    def consistency(self) -> float:
        """Gets the consistency of this DataUtility.


        :return: The consistency of this DataUtility.
        :rtype: float
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency: float):
        """Sets the consistency of this DataUtility.


        :param consistency: The consistency of this DataUtility.
        :type consistency: float
        """
        if consistency is None:
            raise ValueError("Invalid value for `consistency`, must not be `None`")  # noqa: E501

        self._consistency = consistency

    @property
    def completeness(self) -> float:
        """Gets the completeness of this DataUtility.


        :return: The completeness of this DataUtility.
        :rtype: float
        """
        return self._completeness

    @completeness.setter
    def completeness(self, completeness: float):
        """Sets the completeness of this DataUtility.


        :param completeness: The completeness of this DataUtility.
        :type completeness: float
        """
        if completeness is None:
            raise ValueError("Invalid value for `completeness`, must not be `None`")  # noqa: E501

        self._completeness = completeness

    @property
    def timeliness(self) -> float:
        """Gets the timeliness of this DataUtility.


        :return: The timeliness of this DataUtility.
        :rtype: float
        """
        return self._timeliness

    @timeliness.setter
    def timeliness(self, timeliness: float):
        """Sets the timeliness of this DataUtility.


        :param timeliness: The timeliness of this DataUtility.
        :type timeliness: float
        """
        if timeliness is None:
            raise ValueError("Invalid value for `timeliness`, must not be `None`")  # noqa: E501

        self._timeliness = timeliness
