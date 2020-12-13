# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amount import Amount  # noqa: F401,E501
from swagger_server import util


class AllOfStatementMinimumPaymentDue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount: int=None, currency_code: int=986):  # noqa: E501
        """AllOfStatementMinimumPaymentDue - a model defined in Swagger

        :param amount: The amount of this AllOfStatementMinimumPaymentDue.  # noqa: E501
        :type amount: int
        :param currency_code: The currency_code of this AllOfStatementMinimumPaymentDue.  # noqa: E501
        :type currency_code: int
        """
        self.swagger_types = {
            'amount': int,
            'currency_code': int
        }

        self.attribute_map = {
            'amount': 'amount',
            'currency_code': 'currencyCode'
        }
        self._amount = amount
        self._currency_code = currency_code

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfStatementMinimumPaymentDue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfStatementMinimumPaymentDue of this AllOfStatementMinimumPaymentDue.  # noqa: E501
        :rtype: AllOfStatementMinimumPaymentDue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> int:
        """Gets the amount of this AllOfStatementMinimumPaymentDue.

        Valor omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \"amount\":123  # noqa: E501

        :return: The amount of this AllOfStatementMinimumPaymentDue.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this AllOfStatementMinimumPaymentDue.

        Valor omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \"amount\":123  # noqa: E501

        :param amount: The amount of this AllOfStatementMinimumPaymentDue.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency_code(self) -> int:
        """Gets the currency_code of this AllOfStatementMinimumPaymentDue.

        Código da moeda, conforme ISO-4217  # noqa: E501

        :return: The currency_code of this AllOfStatementMinimumPaymentDue.
        :rtype: int
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: int):
        """Sets the currency_code of this AllOfStatementMinimumPaymentDue.

        Código da moeda, conforme ISO-4217  # noqa: E501

        :param currency_code: The currency_code of this AllOfStatementMinimumPaymentDue.
        :type currency_code: int
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code
