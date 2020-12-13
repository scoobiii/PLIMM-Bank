# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.composed_virtual_card_info import ComposedVirtualCardInfo  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class ListVirtualCardsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfListVirtualCardsResponseResultData=None, virtual_cards_count: int=None, virtual_cards: List[ComposedVirtualCardInfo]=None):  # noqa: E501
        """ListVirtualCardsResponse - a model defined in Swagger

        :param result_data: The result_data of this ListVirtualCardsResponse.  # noqa: E501
        :type result_data: AllOfListVirtualCardsResponseResultData
        :param virtual_cards_count: The virtual_cards_count of this ListVirtualCardsResponse.  # noqa: E501
        :type virtual_cards_count: int
        :param virtual_cards: The virtual_cards of this ListVirtualCardsResponse.  # noqa: E501
        :type virtual_cards: List[ComposedVirtualCardInfo]
        """
        self.swagger_types = {
            'result_data': AllOfListVirtualCardsResponseResultData,
            'virtual_cards_count': int,
            'virtual_cards': List[ComposedVirtualCardInfo]
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'virtual_cards_count': 'virtual_cards_count',
            'virtual_cards': 'virtual_cards'
        }
        self._result_data = result_data
        self._virtual_cards_count = virtual_cards_count
        self._virtual_cards = virtual_cards

    @classmethod
    def from_dict(cls, dikt) -> 'ListVirtualCardsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListVirtualCardsResponse of this ListVirtualCardsResponse.  # noqa: E501
        :rtype: ListVirtualCardsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfListVirtualCardsResponseResultData:
        """Gets the result_data of this ListVirtualCardsResponse.


        :return: The result_data of this ListVirtualCardsResponse.
        :rtype: AllOfListVirtualCardsResponseResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfListVirtualCardsResponseResultData):
        """Sets the result_data of this ListVirtualCardsResponse.


        :param result_data: The result_data of this ListVirtualCardsResponse.
        :type result_data: AllOfListVirtualCardsResponseResultData
        """

        self._result_data = result_data

    @property
    def virtual_cards_count(self) -> int:
        """Gets the virtual_cards_count of this ListVirtualCardsResponse.

        Contagem dos cartões virtuais  # noqa: E501

        :return: The virtual_cards_count of this ListVirtualCardsResponse.
        :rtype: int
        """
        return self._virtual_cards_count

    @virtual_cards_count.setter
    def virtual_cards_count(self, virtual_cards_count: int):
        """Sets the virtual_cards_count of this ListVirtualCardsResponse.

        Contagem dos cartões virtuais  # noqa: E501

        :param virtual_cards_count: The virtual_cards_count of this ListVirtualCardsResponse.
        :type virtual_cards_count: int
        """

        self._virtual_cards_count = virtual_cards_count

    @property
    def virtual_cards(self) -> List[ComposedVirtualCardInfo]:
        """Gets the virtual_cards of this ListVirtualCardsResponse.

        Lista de cartões virtuais para o cartão real solicitado  # noqa: E501

        :return: The virtual_cards of this ListVirtualCardsResponse.
        :rtype: List[ComposedVirtualCardInfo]
        """
        return self._virtual_cards

    @virtual_cards.setter
    def virtual_cards(self, virtual_cards: List[ComposedVirtualCardInfo]):
        """Sets the virtual_cards of this ListVirtualCardsResponse.

        Lista de cartões virtuais para o cartão real solicitado  # noqa: E501

        :param virtual_cards: The virtual_cards of this ListVirtualCardsResponse.
        :type virtual_cards: List[ComposedVirtualCardInfo]
        """

        self._virtual_cards = virtual_cards
