# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.cet import CET  # noqa: F401,E501
from swagger_server.models.cet_lateness import CETLateness  # noqa: F401,E501
from swagger_server import util


class FeesAndCET(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, revolving_credit: CET=None, statement_installment_financing: CET=None, cash_withdrawal: CET=None, lateness_interest: CETLateness=None):  # noqa: E501
        """FeesAndCET - a model defined in Swagger

        :param revolving_credit: The revolving_credit of this FeesAndCET.  # noqa: E501
        :type revolving_credit: CET
        :param statement_installment_financing: The statement_installment_financing of this FeesAndCET.  # noqa: E501
        :type statement_installment_financing: CET
        :param cash_withdrawal: The cash_withdrawal of this FeesAndCET.  # noqa: E501
        :type cash_withdrawal: CET
        :param lateness_interest: The lateness_interest of this FeesAndCET.  # noqa: E501
        :type lateness_interest: CETLateness
        """
        self.swagger_types = {
            'revolving_credit': CET,
            'statement_installment_financing': CET,
            'cash_withdrawal': CET,
            'lateness_interest': CETLateness
        }

        self.attribute_map = {
            'revolving_credit': 'revolvingCredit',
            'statement_installment_financing': 'statementInstallmentFinancing',
            'cash_withdrawal': 'cashWithdrawal',
            'lateness_interest': 'latenessInterest'
        }
        self._revolving_credit = revolving_credit
        self._statement_installment_financing = statement_installment_financing
        self._cash_withdrawal = cash_withdrawal
        self._lateness_interest = lateness_interest

    @classmethod
    def from_dict(cls, dikt) -> 'FeesAndCET':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeesAndCET of this FeesAndCET.  # noqa: E501
        :rtype: FeesAndCET
        """
        return util.deserialize_model(dikt, cls)

    @property
    def revolving_credit(self) -> CET:
        """Gets the revolving_credit of this FeesAndCET.


        :return: The revolving_credit of this FeesAndCET.
        :rtype: CET
        """
        return self._revolving_credit

    @revolving_credit.setter
    def revolving_credit(self, revolving_credit: CET):
        """Sets the revolving_credit of this FeesAndCET.


        :param revolving_credit: The revolving_credit of this FeesAndCET.
        :type revolving_credit: CET
        """
        if revolving_credit is None:
            raise ValueError("Invalid value for `revolving_credit`, must not be `None`")  # noqa: E501

        self._revolving_credit = revolving_credit

    @property
    def statement_installment_financing(self) -> CET:
        """Gets the statement_installment_financing of this FeesAndCET.


        :return: The statement_installment_financing of this FeesAndCET.
        :rtype: CET
        """
        return self._statement_installment_financing

    @statement_installment_financing.setter
    def statement_installment_financing(self, statement_installment_financing: CET):
        """Sets the statement_installment_financing of this FeesAndCET.


        :param statement_installment_financing: The statement_installment_financing of this FeesAndCET.
        :type statement_installment_financing: CET
        """

        self._statement_installment_financing = statement_installment_financing

    @property
    def cash_withdrawal(self) -> CET:
        """Gets the cash_withdrawal of this FeesAndCET.


        :return: The cash_withdrawal of this FeesAndCET.
        :rtype: CET
        """
        return self._cash_withdrawal

    @cash_withdrawal.setter
    def cash_withdrawal(self, cash_withdrawal: CET):
        """Sets the cash_withdrawal of this FeesAndCET.


        :param cash_withdrawal: The cash_withdrawal of this FeesAndCET.
        :type cash_withdrawal: CET
        """

        self._cash_withdrawal = cash_withdrawal

    @property
    def lateness_interest(self) -> CETLateness:
        """Gets the lateness_interest of this FeesAndCET.


        :return: The lateness_interest of this FeesAndCET.
        :rtype: CETLateness
        """
        return self._lateness_interest

    @lateness_interest.setter
    def lateness_interest(self, lateness_interest: CETLateness):
        """Sets the lateness_interest of this FeesAndCET.


        :param lateness_interest: The lateness_interest of this FeesAndCET.
        :type lateness_interest: CETLateness
        """
        if lateness_interest is None:
            raise ValueError("Invalid value for `lateness_interest`, must not be `None`")  # noqa: E501

        self._lateness_interest = lateness_interest
