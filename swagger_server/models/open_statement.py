# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server.models.statement_entry import StatementEntry  # noqa: F401,E501
from swagger_server import util


class OpenStatement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_id: str=None, payment_due: str=None, close_date: str=None, previous_balance: AllOfOpenStatementPreviousBalance=None, balance: AllOfOpenStatementBalance=None, credit_limit: AllOfOpenStatementCreditLimit=None, withdrawal_credit_limit: AllOfOpenStatementWithdrawalCreditLimit=None, current_credit_limit: AllOfOpenStatementCurrentCreditLimit=None, current_withdrawal_credit_limit: AllOfOpenStatementCurrentWithdrawalCreditLimit=None, transactions_list: List[StatementEntry]=None, query_date: datetime=None, source_audit: SourceAudit=None):  # noqa: E501
        """OpenStatement - a model defined in Swagger

        :param account_id: The account_id of this OpenStatement.  # noqa: E501
        :type account_id: str
        :param payment_due: The payment_due of this OpenStatement.  # noqa: E501
        :type payment_due: str
        :param close_date: The close_date of this OpenStatement.  # noqa: E501
        :type close_date: str
        :param previous_balance: The previous_balance of this OpenStatement.  # noqa: E501
        :type previous_balance: AllOfOpenStatementPreviousBalance
        :param balance: The balance of this OpenStatement.  # noqa: E501
        :type balance: AllOfOpenStatementBalance
        :param credit_limit: The credit_limit of this OpenStatement.  # noqa: E501
        :type credit_limit: AllOfOpenStatementCreditLimit
        :param withdrawal_credit_limit: The withdrawal_credit_limit of this OpenStatement.  # noqa: E501
        :type withdrawal_credit_limit: AllOfOpenStatementWithdrawalCreditLimit
        :param current_credit_limit: The current_credit_limit of this OpenStatement.  # noqa: E501
        :type current_credit_limit: AllOfOpenStatementCurrentCreditLimit
        :param current_withdrawal_credit_limit: The current_withdrawal_credit_limit of this OpenStatement.  # noqa: E501
        :type current_withdrawal_credit_limit: AllOfOpenStatementCurrentWithdrawalCreditLimit
        :param transactions_list: The transactions_list of this OpenStatement.  # noqa: E501
        :type transactions_list: List[StatementEntry]
        :param query_date: The query_date of this OpenStatement.  # noqa: E501
        :type query_date: datetime
        :param source_audit: The source_audit of this OpenStatement.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'account_id': str,
            'payment_due': str,
            'close_date': str,
            'previous_balance': AllOfOpenStatementPreviousBalance,
            'balance': AllOfOpenStatementBalance,
            'credit_limit': AllOfOpenStatementCreditLimit,
            'withdrawal_credit_limit': AllOfOpenStatementWithdrawalCreditLimit,
            'current_credit_limit': AllOfOpenStatementCurrentCreditLimit,
            'current_withdrawal_credit_limit': AllOfOpenStatementCurrentWithdrawalCreditLimit,
            'transactions_list': List[StatementEntry],
            'query_date': datetime,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'payment_due': 'paymentDue',
            'close_date': 'closeDate',
            'previous_balance': 'previousBalance',
            'balance': 'balance',
            'credit_limit': 'creditLimit',
            'withdrawal_credit_limit': 'withdrawalCreditLimit',
            'current_credit_limit': 'currentCreditLimit',
            'current_withdrawal_credit_limit': 'currentWithdrawalCreditLimit',
            'transactions_list': 'transactionsList',
            'query_date': 'query_date',
            'source_audit': 'sourceAudit'
        }
        self._account_id = account_id
        self._payment_due = payment_due
        self._close_date = close_date
        self._previous_balance = previous_balance
        self._balance = balance
        self._credit_limit = credit_limit
        self._withdrawal_credit_limit = withdrawal_credit_limit
        self._current_credit_limit = current_credit_limit
        self._current_withdrawal_credit_limit = current_withdrawal_credit_limit
        self._transactions_list = transactions_list
        self._query_date = query_date
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'OpenStatement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OpenStatement of this OpenStatement.  # noqa: E501
        :rtype: OpenStatement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self) -> str:
        """Gets the account_id of this OpenStatement.

        Identificador único da conta.  # noqa: E501

        :return: The account_id of this OpenStatement.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this OpenStatement.

        Identificador único da conta.  # noqa: E501

        :param account_id: The account_id of this OpenStatement.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def payment_due(self) -> str:
        """Gets the payment_due of this OpenStatement.

        Data de vencimento da fatura.  # noqa: E501

        :return: The payment_due of this OpenStatement.
        :rtype: str
        """
        return self._payment_due

    @payment_due.setter
    def payment_due(self, payment_due: str):
        """Sets the payment_due of this OpenStatement.

        Data de vencimento da fatura.  # noqa: E501

        :param payment_due: The payment_due of this OpenStatement.
        :type payment_due: str
        """
        if payment_due is None:
            raise ValueError("Invalid value for `payment_due`, must not be `None`")  # noqa: E501

        self._payment_due = payment_due

    @property
    def close_date(self) -> str:
        """Gets the close_date of this OpenStatement.

        Data de fechamento da fatura.  # noqa: E501

        :return: The close_date of this OpenStatement.
        :rtype: str
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date: str):
        """Sets the close_date of this OpenStatement.

        Data de fechamento da fatura.  # noqa: E501

        :param close_date: The close_date of this OpenStatement.
        :type close_date: str
        """

        self._close_date = close_date

    @property
    def previous_balance(self) -> AllOfOpenStatementPreviousBalance:
        """Gets the previous_balance of this OpenStatement.

        Saldo da fatura anterior  # noqa: E501

        :return: The previous_balance of this OpenStatement.
        :rtype: AllOfOpenStatementPreviousBalance
        """
        return self._previous_balance

    @previous_balance.setter
    def previous_balance(self, previous_balance: AllOfOpenStatementPreviousBalance):
        """Sets the previous_balance of this OpenStatement.

        Saldo da fatura anterior  # noqa: E501

        :param previous_balance: The previous_balance of this OpenStatement.
        :type previous_balance: AllOfOpenStatementPreviousBalance
        """

        self._previous_balance = previous_balance

    @property
    def balance(self) -> AllOfOpenStatementBalance:
        """Gets the balance of this OpenStatement.

        Saldo total da fatura  # noqa: E501

        :return: The balance of this OpenStatement.
        :rtype: AllOfOpenStatementBalance
        """
        return self._balance

    @balance.setter
    def balance(self, balance: AllOfOpenStatementBalance):
        """Sets the balance of this OpenStatement.

        Saldo total da fatura  # noqa: E501

        :param balance: The balance of this OpenStatement.
        :type balance: AllOfOpenStatementBalance
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def credit_limit(self) -> AllOfOpenStatementCreditLimit:
        """Gets the credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite de crédito atribuído à conta pelo emissor.  # noqa: E501

        :return: The credit_limit of this OpenStatement.
        :rtype: AllOfOpenStatementCreditLimit
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit: AllOfOpenStatementCreditLimit):
        """Sets the credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite de crédito atribuído à conta pelo emissor.  # noqa: E501

        :param credit_limit: The credit_limit of this OpenStatement.
        :type credit_limit: AllOfOpenStatementCreditLimit
        """
        if credit_limit is None:
            raise ValueError("Invalid value for `credit_limit`, must not be `None`")  # noqa: E501

        self._credit_limit = credit_limit

    @property
    def withdrawal_credit_limit(self) -> AllOfOpenStatementWithdrawalCreditLimit:
        """Gets the withdrawal_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite de crédito para saques atribuído à conta pelo emissor.  # noqa: E501

        :return: The withdrawal_credit_limit of this OpenStatement.
        :rtype: AllOfOpenStatementWithdrawalCreditLimit
        """
        return self._withdrawal_credit_limit

    @withdrawal_credit_limit.setter
    def withdrawal_credit_limit(self, withdrawal_credit_limit: AllOfOpenStatementWithdrawalCreditLimit):
        """Sets the withdrawal_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite de crédito para saques atribuído à conta pelo emissor.  # noqa: E501

        :param withdrawal_credit_limit: The withdrawal_credit_limit of this OpenStatement.
        :type withdrawal_credit_limit: AllOfOpenStatementWithdrawalCreditLimit
        """
        if withdrawal_credit_limit is None:
            raise ValueError("Invalid value for `withdrawal_credit_limit`, must not be `None`")  # noqa: E501

        self._withdrawal_credit_limit = withdrawal_credit_limit

    @property
    def current_credit_limit(self) -> AllOfOpenStatementCurrentCreditLimit:
        """Gets the current_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor do limite disponível atualmente para a conta, já descontando o saldo.  # noqa: E501

        :return: The current_credit_limit of this OpenStatement.
        :rtype: AllOfOpenStatementCurrentCreditLimit
        """
        return self._current_credit_limit

    @current_credit_limit.setter
    def current_credit_limit(self, current_credit_limit: AllOfOpenStatementCurrentCreditLimit):
        """Sets the current_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor do limite disponível atualmente para a conta, já descontando o saldo.  # noqa: E501

        :param current_credit_limit: The current_credit_limit of this OpenStatement.
        :type current_credit_limit: AllOfOpenStatementCurrentCreditLimit
        """
        if current_credit_limit is None:
            raise ValueError("Invalid value for `current_credit_limit`, must not be `None`")  # noqa: E501

        self._current_credit_limit = current_credit_limit

    @property
    def current_withdrawal_credit_limit(self) -> AllOfOpenStatementCurrentWithdrawalCreditLimit:
        """Gets the current_withdrawal_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite atualmente disponível para saques, j´descontando gastos.  # noqa: E501

        :return: The current_withdrawal_credit_limit of this OpenStatement.
        :rtype: AllOfOpenStatementCurrentWithdrawalCreditLimit
        """
        return self._current_withdrawal_credit_limit

    @current_withdrawal_credit_limit.setter
    def current_withdrawal_credit_limit(self, current_withdrawal_credit_limit: AllOfOpenStatementCurrentWithdrawalCreditLimit):
        """Sets the current_withdrawal_credit_limit of this OpenStatement.

        Para produtos de crédito pós-pago: Valor limite atualmente disponível para saques, j´descontando gastos.  # noqa: E501

        :param current_withdrawal_credit_limit: The current_withdrawal_credit_limit of this OpenStatement.
        :type current_withdrawal_credit_limit: AllOfOpenStatementCurrentWithdrawalCreditLimit
        """
        if current_withdrawal_credit_limit is None:
            raise ValueError("Invalid value for `current_withdrawal_credit_limit`, must not be `None`")  # noqa: E501

        self._current_withdrawal_credit_limit = current_withdrawal_credit_limit

    @property
    def transactions_list(self) -> List[StatementEntry]:
        """Gets the transactions_list of this OpenStatement.

        Lista de lançamentos em aberto  # noqa: E501

        :return: The transactions_list of this OpenStatement.
        :rtype: List[StatementEntry]
        """
        return self._transactions_list

    @transactions_list.setter
    def transactions_list(self, transactions_list: List[StatementEntry]):
        """Sets the transactions_list of this OpenStatement.

        Lista de lançamentos em aberto  # noqa: E501

        :param transactions_list: The transactions_list of this OpenStatement.
        :type transactions_list: List[StatementEntry]
        """
        if transactions_list is None:
            raise ValueError("Invalid value for `transactions_list`, must not be `None`")  # noqa: E501

        self._transactions_list = transactions_list

    @property
    def query_date(self) -> datetime:
        """Gets the query_date of this OpenStatement.

        Data de consulta.  # noqa: E501

        :return: The query_date of this OpenStatement.
        :rtype: datetime
        """
        return self._query_date

    @query_date.setter
    def query_date(self, query_date: datetime):
        """Sets the query_date of this OpenStatement.

        Data de consulta.  # noqa: E501

        :param query_date: The query_date of this OpenStatement.
        :type query_date: datetime
        """

        self._query_date = query_date

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this OpenStatement.


        :return: The source_audit of this OpenStatement.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this OpenStatement.


        :param source_audit: The source_audit of this OpenStatement.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit
