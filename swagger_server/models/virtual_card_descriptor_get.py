# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VirtualCardDescriptorGet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, v_card_id: str=None, v_date_exp: str=None):  # noqa: E501
        """VirtualCardDescriptorGet - a model defined in Swagger

        :param v_card_id: The v_card_id of this VirtualCardDescriptorGet.  # noqa: E501
        :type v_card_id: str
        :param v_date_exp: The v_date_exp of this VirtualCardDescriptorGet.  # noqa: E501
        :type v_date_exp: str
        """
        self.swagger_types = {
            'v_card_id': str,
            'v_date_exp': str
        }

        self.attribute_map = {
            'v_card_id': 'vCardId',
            'v_date_exp': 'vDateExp'
        }
        self._v_card_id = v_card_id
        self._v_date_exp = v_date_exp

    @classmethod
    def from_dict(cls, dikt) -> 'VirtualCardDescriptorGet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VirtualCardDescriptorGet of this VirtualCardDescriptorGet.  # noqa: E501
        :rtype: VirtualCardDescriptorGet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def v_card_id(self) -> str:
        """Gets the v_card_id of this VirtualCardDescriptorGet.

        Identificador único do cartão virtual gerado pela paySmart  # noqa: E501

        :return: The v_card_id of this VirtualCardDescriptorGet.
        :rtype: str
        """
        return self._v_card_id

    @v_card_id.setter
    def v_card_id(self, v_card_id: str):
        """Sets the v_card_id of this VirtualCardDescriptorGet.

        Identificador único do cartão virtual gerado pela paySmart  # noqa: E501

        :param v_card_id: The v_card_id of this VirtualCardDescriptorGet.
        :type v_card_id: str
        """

        self._v_card_id = v_card_id

    @property
    def v_date_exp(self) -> str:
        """Gets the v_date_exp of this VirtualCardDescriptorGet.

        Data de expiração do cartão virtual no formato MM/yyyy  # noqa: E501

        :return: The v_date_exp of this VirtualCardDescriptorGet.
        :rtype: str
        """
        return self._v_date_exp

    @v_date_exp.setter
    def v_date_exp(self, v_date_exp: str):
        """Sets the v_date_exp of this VirtualCardDescriptorGet.

        Data de expiração do cartão virtual no formato MM/yyyy  # noqa: E501

        :param v_date_exp: The v_date_exp of this VirtualCardDescriptorGet.
        :type v_date_exp: str
        """

        self._v_date_exp = v_date_exp
