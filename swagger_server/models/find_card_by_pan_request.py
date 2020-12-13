# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FindCardByPANRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pan: str=None):  # noqa: E501
        """FindCardByPANRequest - a model defined in Swagger

        :param pan: The pan of this FindCardByPANRequest.  # noqa: E501
        :type pan: str
        """
        self.swagger_types = {
            'pan': str
        }

        self.attribute_map = {
            'pan': 'PAN'
        }
        self._pan = pan

    @classmethod
    def from_dict(cls, dikt) -> 'FindCardByPANRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FindCardByPANRequest of this FindCardByPANRequest.  # noqa: E501
        :rtype: FindCardByPANRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pan(self) -> str:
        """Gets the pan of this FindCardByPANRequest.

        Número do cartão.  # noqa: E501

        :return: The pan of this FindCardByPANRequest.
        :rtype: str
        """
        return self._pan

    @pan.setter
    def pan(self, pan: str):
        """Sets the pan of this FindCardByPANRequest.

        Número do cartão.  # noqa: E501

        :param pan: The pan of this FindCardByPANRequest.
        :type pan: str
        """
        if pan is None:
            raise ValueError("Invalid value for `pan`, must not be `None`")  # noqa: E501

        self._pan = pan
