# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class NewCardrequestCreatedSuccessfully(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfNewCardrequestCreatedSuccessfullyResultData=None, card_id: str=None):  # noqa: E501
        """NewCardrequestCreatedSuccessfully - a model defined in Swagger

        :param result_data: The result_data of this NewCardrequestCreatedSuccessfully.  # noqa: E501
        :type result_data: AllOfNewCardrequestCreatedSuccessfullyResultData
        :param card_id: The card_id of this NewCardrequestCreatedSuccessfully.  # noqa: E501
        :type card_id: str
        """
        self.swagger_types = {
            'result_data': AllOfNewCardrequestCreatedSuccessfullyResultData,
            'card_id': str
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'card_id': 'cardId'
        }
        self._result_data = result_data
        self._card_id = card_id

    @classmethod
    def from_dict(cls, dikt) -> 'NewCardrequestCreatedSuccessfully':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewCardrequestCreatedSuccessfully of this NewCardrequestCreatedSuccessfully.  # noqa: E501
        :rtype: NewCardrequestCreatedSuccessfully
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfNewCardrequestCreatedSuccessfullyResultData:
        """Gets the result_data of this NewCardrequestCreatedSuccessfully.


        :return: The result_data of this NewCardrequestCreatedSuccessfully.
        :rtype: AllOfNewCardrequestCreatedSuccessfullyResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfNewCardrequestCreatedSuccessfullyResultData):
        """Sets the result_data of this NewCardrequestCreatedSuccessfully.


        :param result_data: The result_data of this NewCardrequestCreatedSuccessfully.
        :type result_data: AllOfNewCardrequestCreatedSuccessfullyResultData
        """

        self._result_data = result_data

    @property
    def card_id(self) -> str:
        """Gets the card_id of this NewCardrequestCreatedSuccessfully.

        Identificador único do cartão. Pode ser usado para verificar o status da requisição e para consultar dados do cartão uma vez que ele tenha sido emitido.  # noqa: E501

        :return: The card_id of this NewCardrequestCreatedSuccessfully.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id: str):
        """Sets the card_id of this NewCardrequestCreatedSuccessfully.

        Identificador único do cartão. Pode ser usado para verificar o status da requisição e para consultar dados do cartão uma vez que ele tenha sido emitido.  # noqa: E501

        :param card_id: The card_id of this NewCardrequestCreatedSuccessfully.
        :type card_id: str
        """
        if card_id is None:
            raise ValueError("Invalid value for `card_id`, must not be `None`")  # noqa: E501

        self._card_id = card_id
