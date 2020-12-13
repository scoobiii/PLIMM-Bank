# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.card import Card  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class CardBlockAndReissueResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfCardBlockAndReissueResultResultData=None, blocked_card: Card=None, new_card_id: str=None):  # noqa: E501
        """CardBlockAndReissueResult - a model defined in Swagger

        :param result_data: The result_data of this CardBlockAndReissueResult.  # noqa: E501
        :type result_data: AllOfCardBlockAndReissueResultResultData
        :param blocked_card: The blocked_card of this CardBlockAndReissueResult.  # noqa: E501
        :type blocked_card: Card
        :param new_card_id: The new_card_id of this CardBlockAndReissueResult.  # noqa: E501
        :type new_card_id: str
        """
        self.swagger_types = {
            'result_data': AllOfCardBlockAndReissueResultResultData,
            'blocked_card': Card,
            'new_card_id': str
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'blocked_card': 'blocked_card',
            'new_card_id': 'newCardId'
        }
        self._result_data = result_data
        self._blocked_card = blocked_card
        self._new_card_id = new_card_id

    @classmethod
    def from_dict(cls, dikt) -> 'CardBlockAndReissueResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardBlockAndReissueResult of this CardBlockAndReissueResult.  # noqa: E501
        :rtype: CardBlockAndReissueResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfCardBlockAndReissueResultResultData:
        """Gets the result_data of this CardBlockAndReissueResult.


        :return: The result_data of this CardBlockAndReissueResult.
        :rtype: AllOfCardBlockAndReissueResultResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfCardBlockAndReissueResultResultData):
        """Sets the result_data of this CardBlockAndReissueResult.


        :param result_data: The result_data of this CardBlockAndReissueResult.
        :type result_data: AllOfCardBlockAndReissueResultResultData
        """
        if result_data is None:
            raise ValueError("Invalid value for `result_data`, must not be `None`")  # noqa: E501

        self._result_data = result_data

    @property
    def blocked_card(self) -> Card:
        """Gets the blocked_card of this CardBlockAndReissueResult.


        :return: The blocked_card of this CardBlockAndReissueResult.
        :rtype: Card
        """
        return self._blocked_card

    @blocked_card.setter
    def blocked_card(self, blocked_card: Card):
        """Sets the blocked_card of this CardBlockAndReissueResult.


        :param blocked_card: The blocked_card of this CardBlockAndReissueResult.
        :type blocked_card: Card
        """
        if blocked_card is None:
            raise ValueError("Invalid value for `blocked_card`, must not be `None`")  # noqa: E501

        self._blocked_card = blocked_card

    @property
    def new_card_id(self) -> str:
        """Gets the new_card_id of this CardBlockAndReissueResult.

        Identificador único do novo cartão. Pode ser usado para verificar o status da requisição e para consultar dados do cartão uma vez que ele tenha sido emitido.  # noqa: E501

        :return: The new_card_id of this CardBlockAndReissueResult.
        :rtype: str
        """
        return self._new_card_id

    @new_card_id.setter
    def new_card_id(self, new_card_id: str):
        """Sets the new_card_id of this CardBlockAndReissueResult.

        Identificador único do novo cartão. Pode ser usado para verificar o status da requisição e para consultar dados do cartão uma vez que ele tenha sido emitido.  # noqa: E501

        :param new_card_id: The new_card_id of this CardBlockAndReissueResult.
        :type new_card_id: str
        """
        if new_card_id is None:
            raise ValueError("Invalid value for `new_card_id`, must not be `None`")  # noqa: E501

        self._new_card_id = new_card_id
