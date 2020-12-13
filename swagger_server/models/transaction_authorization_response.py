# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class TransactionAuthorizationResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, approved: bool=None, denial_reason: AllOfTransactionAuthorizationResponseDenialReason=None):  # noqa: E501
        """TransactionAuthorizationResponse - a model defined in Swagger

        :param approved: The approved of this TransactionAuthorizationResponse.  # noqa: E501
        :type approved: bool
        :param denial_reason: The denial_reason of this TransactionAuthorizationResponse.  # noqa: E501
        :type denial_reason: AllOfTransactionAuthorizationResponseDenialReason
        """
        self.swagger_types = {
            'approved': bool,
            'denial_reason': AllOfTransactionAuthorizationResponseDenialReason
        }

        self.attribute_map = {
            'approved': 'approved',
            'denial_reason': 'denialReason'
        }
        self._approved = approved
        self._denial_reason = denial_reason

    @classmethod
    def from_dict(cls, dikt) -> 'TransactionAuthorizationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransactionAuthorizationResponse of this TransactionAuthorizationResponse.  # noqa: E501
        :rtype: TransactionAuthorizationResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def approved(self) -> bool:
        """Gets the approved of this TransactionAuthorizationResponse.

        Indica se a transação foi aprovada pelo autorizador.  # noqa: E501

        :return: The approved of this TransactionAuthorizationResponse.
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved: bool):
        """Sets the approved of this TransactionAuthorizationResponse.

        Indica se a transação foi aprovada pelo autorizador.  # noqa: E501

        :param approved: The approved of this TransactionAuthorizationResponse.
        :type approved: bool
        """

        self._approved = approved

    @property
    def denial_reason(self) -> AllOfTransactionAuthorizationResponseDenialReason:
        """Gets the denial_reason of this TransactionAuthorizationResponse.

        Razão da negação. Só presente se a approved for false.  # noqa: E501

        :return: The denial_reason of this TransactionAuthorizationResponse.
        :rtype: AllOfTransactionAuthorizationResponseDenialReason
        """
        return self._denial_reason

    @denial_reason.setter
    def denial_reason(self, denial_reason: AllOfTransactionAuthorizationResponseDenialReason):
        """Sets the denial_reason of this TransactionAuthorizationResponse.

        Razão da negação. Só presente se a approved for false.  # noqa: E501

        :param denial_reason: The denial_reason of this TransactionAuthorizationResponse.
        :type denial_reason: AllOfTransactionAuthorizationResponseDenialReason
        """

        self._denial_reason = denial_reason
