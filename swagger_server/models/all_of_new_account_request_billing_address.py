# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.address import Address  # noqa: F401,E501
from swagger_server import util


class AllOfNewAccountRequestBillingAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address_line1: str=None, address_line2: str=None, address_line3: str=None, reference: str=None, neighborhood: str=None, city: str=None, state: str=None, zipcode: str=None, country: str='Brasil'):  # noqa: E501
        """AllOfNewAccountRequestBillingAddress - a model defined in Swagger

        :param address_line1: The address_line1 of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type address_line1: str
        :param address_line2: The address_line2 of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type address_line2: str
        :param address_line3: The address_line3 of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type address_line3: str
        :param reference: The reference of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type reference: str
        :param neighborhood: The neighborhood of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type neighborhood: str
        :param city: The city of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type city: str
        :param state: The state of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type state: str
        :param zipcode: The zipcode of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type zipcode: str
        :param country: The country of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :type country: str
        """
        self.swagger_types = {
            'address_line1': str,
            'address_line2': str,
            'address_line3': str,
            'reference': str,
            'neighborhood': str,
            'city': str,
            'state': str,
            'zipcode': str,
            'country': str
        }

        self.attribute_map = {
            'address_line1': 'addressLine1',
            'address_line2': 'addressLine2',
            'address_line3': 'addressLine3',
            'reference': 'reference',
            'neighborhood': 'neighborhood',
            'city': 'city',
            'state': 'state',
            'zipcode': 'zipcode',
            'country': 'country'
        }
        self._address_line1 = address_line1
        self._address_line2 = address_line2
        self._address_line3 = address_line3
        self._reference = reference
        self._neighborhood = neighborhood
        self._city = city
        self._state = state
        self._zipcode = zipcode
        self._country = country

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfNewAccountRequestBillingAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfNewAccountRequestBillingAddress of this AllOfNewAccountRequestBillingAddress.  # noqa: E501
        :rtype: AllOfNewAccountRequestBillingAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_line1(self) -> str:
        """Gets the address_line1 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Nome da rua.  # noqa: E501

        :return: The address_line1 of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1: str):
        """Sets the address_line1 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Nome da rua.  # noqa: E501

        :param address_line1: The address_line1 of this AllOfNewAccountRequestBillingAddress.
        :type address_line1: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self) -> str:
        """Gets the address_line2 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Número da rua.  # noqa: E501

        :return: The address_line2 of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2: str):
        """Sets the address_line2 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Número da rua.  # noqa: E501

        :param address_line2: The address_line2 of this AllOfNewAccountRequestBillingAddress.
        :type address_line2: str
        """

        self._address_line2 = address_line2

    @property
    def address_line3(self) -> str:
        """Gets the address_line3 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Complemento.  # noqa: E501

        :return: The address_line3 of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3: str):
        """Sets the address_line3 of this AllOfNewAccountRequestBillingAddress.

        Endereço. Complemento.  # noqa: E501

        :param address_line3: The address_line3 of this AllOfNewAccountRequestBillingAddress.
        :type address_line3: str
        """

        self._address_line3 = address_line3

    @property
    def reference(self) -> str:
        """Gets the reference of this AllOfNewAccountRequestBillingAddress.

        Referência próxima para auxílio na localização.  # noqa: E501

        :return: The reference of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this AllOfNewAccountRequestBillingAddress.

        Referência próxima para auxílio na localização.  # noqa: E501

        :param reference: The reference of this AllOfNewAccountRequestBillingAddress.
        :type reference: str
        """

        self._reference = reference

    @property
    def neighborhood(self) -> str:
        """Gets the neighborhood of this AllOfNewAccountRequestBillingAddress.

        Bairro.  # noqa: E501

        :return: The neighborhood of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str):
        """Sets the neighborhood of this AllOfNewAccountRequestBillingAddress.

        Bairro.  # noqa: E501

        :param neighborhood: The neighborhood of this AllOfNewAccountRequestBillingAddress.
        :type neighborhood: str
        """

        self._neighborhood = neighborhood

    @property
    def city(self) -> str:
        """Gets the city of this AllOfNewAccountRequestBillingAddress.

        Cidade.  # noqa: E501

        :return: The city of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this AllOfNewAccountRequestBillingAddress.

        Cidade.  # noqa: E501

        :param city: The city of this AllOfNewAccountRequestBillingAddress.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self) -> str:
        """Gets the state of this AllOfNewAccountRequestBillingAddress.

        Estado.  # noqa: E501

        :return: The state of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this AllOfNewAccountRequestBillingAddress.

        Estado.  # noqa: E501

        :param state: The state of this AllOfNewAccountRequestBillingAddress.
        :type state: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def zipcode(self) -> str:
        """Gets the zipcode of this AllOfNewAccountRequestBillingAddress.

        CEP.  # noqa: E501

        :return: The zipcode of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode: str):
        """Sets the zipcode of this AllOfNewAccountRequestBillingAddress.

        CEP.  # noqa: E501

        :param zipcode: The zipcode of this AllOfNewAccountRequestBillingAddress.
        :type zipcode: str
        """

        self._zipcode = zipcode

    @property
    def country(self) -> str:
        """Gets the country of this AllOfNewAccountRequestBillingAddress.

        País.  # noqa: E501

        :return: The country of this AllOfNewAccountRequestBillingAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this AllOfNewAccountRequestBillingAddress.

        País.  # noqa: E501

        :param country: The country of this AllOfNewAccountRequestBillingAddress.
        :type country: str
        """

        self._country = country
