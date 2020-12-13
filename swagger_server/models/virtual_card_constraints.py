# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VirtualCardConstraints(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, currency_code: str='986', max_amount: str=None, usage_limit: str=None, expiration_timestamp: str=None):  # noqa: E501
        """VirtualCardConstraints - a model defined in Swagger

        :param currency_code: The currency_code of this VirtualCardConstraints.  # noqa: E501
        :type currency_code: str
        :param max_amount: The max_amount of this VirtualCardConstraints.  # noqa: E501
        :type max_amount: str
        :param usage_limit: The usage_limit of this VirtualCardConstraints.  # noqa: E501
        :type usage_limit: str
        :param expiration_timestamp: The expiration_timestamp of this VirtualCardConstraints.  # noqa: E501
        :type expiration_timestamp: str
        """
        self.swagger_types = {
            'currency_code': str,
            'max_amount': str,
            'usage_limit': str,
            'expiration_timestamp': str
        }

        self.attribute_map = {
            'currency_code': 'currency_code',
            'max_amount': 'max_amount',
            'usage_limit': 'usage_limit',
            'expiration_timestamp': 'expiration_timestamp'
        }
        self._currency_code = currency_code
        self._max_amount = max_amount
        self._usage_limit = usage_limit
        self._expiration_timestamp = expiration_timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'VirtualCardConstraints':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VirtualCardConstraints of this VirtualCardConstraints.  # noqa: E501
        :rtype: VirtualCardConstraints
        """
        return util.deserialize_model(dikt, cls)

    @property
    def currency_code(self) -> str:
        """Gets the currency_code of this VirtualCardConstraints.

        Código da moeda, conforme ISO-4217, Se o valor for \"*\" (asterisco), aceita qualquer moeda.  # noqa: E501

        :return: The currency_code of this VirtualCardConstraints.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        """Sets the currency_code of this VirtualCardConstraints.

        Código da moeda, conforme ISO-4217, Se o valor for \"*\" (asterisco), aceita qualquer moeda.  # noqa: E501

        :param currency_code: The currency_code of this VirtualCardConstraints.
        :type currency_code: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def max_amount(self) -> str:
        """Gets the max_amount of this VirtualCardConstraints.

        Valor máximo permitido por transação, incluindo os centavos sem vírgula. Se o valor for \"*\" (asterisco), não há limite superior para o valor das transações.  # noqa: E501

        :return: The max_amount of this VirtualCardConstraints.
        :rtype: str
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount: str):
        """Sets the max_amount of this VirtualCardConstraints.

        Valor máximo permitido por transação, incluindo os centavos sem vírgula. Se o valor for \"*\" (asterisco), não há limite superior para o valor das transações.  # noqa: E501

        :param max_amount: The max_amount of this VirtualCardConstraints.
        :type max_amount: str
        """
        if max_amount is None:
            raise ValueError("Invalid value for `max_amount`, must not be `None`")  # noqa: E501

        self._max_amount = max_amount

    @property
    def usage_limit(self) -> str:
        """Gets the usage_limit of this VirtualCardConstraints.

        Total de transações disponíveis para o Cartão Virtual. Utilize \"*\" (asterisco) para indicar que não deve haver limite no número de transações desse cartão.  # noqa: E501

        :return: The usage_limit of this VirtualCardConstraints.
        :rtype: str
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit: str):
        """Sets the usage_limit of this VirtualCardConstraints.

        Total de transações disponíveis para o Cartão Virtual. Utilize \"*\" (asterisco) para indicar que não deve haver limite no número de transações desse cartão.  # noqa: E501

        :param usage_limit: The usage_limit of this VirtualCardConstraints.
        :type usage_limit: str
        """
        if usage_limit is None:
            raise ValueError("Invalid value for `usage_limit`, must not be `None`")  # noqa: E501

        self._usage_limit = usage_limit

    @property
    def expiration_timestamp(self) -> str:
        """Gets the expiration_timestamp of this VirtualCardConstraints.

        Data de expiração do cartão virtual, no formato YYYY-MM-DD'T'hh:m:ss  # noqa: E501

        :return: The expiration_timestamp of this VirtualCardConstraints.
        :rtype: str
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp: str):
        """Sets the expiration_timestamp of this VirtualCardConstraints.

        Data de expiração do cartão virtual, no formato YYYY-MM-DD'T'hh:m:ss  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this VirtualCardConstraints.
        :type expiration_timestamp: str
        """
        if expiration_timestamp is None:
            raise ValueError("Invalid value for `expiration_timestamp`, must not be `None`")  # noqa: E501

        self._expiration_timestamp = expiration_timestamp
