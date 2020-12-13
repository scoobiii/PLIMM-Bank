# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amount import Amount  # noqa: F401,E501
from swagger_server.models.entry_mode import EntryMode  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.transaction_authorization_response import TransactionAuthorizationResponse  # noqa: F401,E501
from swagger_server.models.transaction_status import TransactionStatus  # noqa: F401,E501
from swagger_server.models.transaction_type import TransactionType  # noqa: F401,E501
from swagger_server import util


class TransactionQueryResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, transaction_id: str=None, account_id: str=None, transaction_date_time: datetime=None, settlement_date_time: datetime=None, transaction_type: TransactionType=None, transaction_status: TransactionStatus=None, transaction_authorization_response: TransactionAuthorizationResponse=None, acquirer_id: str=None, acquirer_transaction_id: str=None, merchant_id: str=None, merchant_name: str=None, merchant_document_id: str=None, merchant_address: str=None, merchant_city: str=None, merchant_uf: str=None, country_code: str=None, mcc: str=None, terminal_id: str=None, amount: Amount=None, entry_mode: EntryMode=None, card: AllOfTransactionQueryResultCard=None, cancelling_transaction_id: str=None):  # noqa: E501
        """TransactionQueryResult - a model defined in Swagger

        :param transaction_id: The transaction_id of this TransactionQueryResult.  # noqa: E501
        :type transaction_id: str
        :param account_id: The account_id of this TransactionQueryResult.  # noqa: E501
        :type account_id: str
        :param transaction_date_time: The transaction_date_time of this TransactionQueryResult.  # noqa: E501
        :type transaction_date_time: datetime
        :param settlement_date_time: The settlement_date_time of this TransactionQueryResult.  # noqa: E501
        :type settlement_date_time: datetime
        :param transaction_type: The transaction_type of this TransactionQueryResult.  # noqa: E501
        :type transaction_type: TransactionType
        :param transaction_status: The transaction_status of this TransactionQueryResult.  # noqa: E501
        :type transaction_status: TransactionStatus
        :param transaction_authorization_response: The transaction_authorization_response of this TransactionQueryResult.  # noqa: E501
        :type transaction_authorization_response: TransactionAuthorizationResponse
        :param acquirer_id: The acquirer_id of this TransactionQueryResult.  # noqa: E501
        :type acquirer_id: str
        :param acquirer_transaction_id: The acquirer_transaction_id of this TransactionQueryResult.  # noqa: E501
        :type acquirer_transaction_id: str
        :param merchant_id: The merchant_id of this TransactionQueryResult.  # noqa: E501
        :type merchant_id: str
        :param merchant_name: The merchant_name of this TransactionQueryResult.  # noqa: E501
        :type merchant_name: str
        :param merchant_document_id: The merchant_document_id of this TransactionQueryResult.  # noqa: E501
        :type merchant_document_id: str
        :param merchant_address: The merchant_address of this TransactionQueryResult.  # noqa: E501
        :type merchant_address: str
        :param merchant_city: The merchant_city of this TransactionQueryResult.  # noqa: E501
        :type merchant_city: str
        :param merchant_uf: The merchant_uf of this TransactionQueryResult.  # noqa: E501
        :type merchant_uf: str
        :param country_code: The country_code of this TransactionQueryResult.  # noqa: E501
        :type country_code: str
        :param mcc: The mcc of this TransactionQueryResult.  # noqa: E501
        :type mcc: str
        :param terminal_id: The terminal_id of this TransactionQueryResult.  # noqa: E501
        :type terminal_id: str
        :param amount: The amount of this TransactionQueryResult.  # noqa: E501
        :type amount: Amount
        :param entry_mode: The entry_mode of this TransactionQueryResult.  # noqa: E501
        :type entry_mode: EntryMode
        :param card: The card of this TransactionQueryResult.  # noqa: E501
        :type card: AllOfTransactionQueryResultCard
        :param cancelling_transaction_id: The cancelling_transaction_id of this TransactionQueryResult.  # noqa: E501
        :type cancelling_transaction_id: str
        """
        self.swagger_types = {
            'transaction_id': str,
            'account_id': str,
            'transaction_date_time': datetime,
            'settlement_date_time': datetime,
            'transaction_type': TransactionType,
            'transaction_status': TransactionStatus,
            'transaction_authorization_response': TransactionAuthorizationResponse,
            'acquirer_id': str,
            'acquirer_transaction_id': str,
            'merchant_id': str,
            'merchant_name': str,
            'merchant_document_id': str,
            'merchant_address': str,
            'merchant_city': str,
            'merchant_uf': str,
            'country_code': str,
            'mcc': str,
            'terminal_id': str,
            'amount': Amount,
            'entry_mode': EntryMode,
            'card': AllOfTransactionQueryResultCard,
            'cancelling_transaction_id': str
        }

        self.attribute_map = {
            'transaction_id': 'transactionId',
            'account_id': 'accountId',
            'transaction_date_time': 'transactionDateTime',
            'settlement_date_time': 'settlementDateTime',
            'transaction_type': 'transactionType',
            'transaction_status': 'transactionStatus',
            'transaction_authorization_response': 'transactionAuthorizationResponse',
            'acquirer_id': 'acquirerId',
            'acquirer_transaction_id': 'acquirerTransactionId',
            'merchant_id': 'merchantId',
            'merchant_name': 'merchantName',
            'merchant_document_id': 'merchantDocumentId',
            'merchant_address': 'merchantAddress',
            'merchant_city': 'merchantCity',
            'merchant_uf': 'merchantUf',
            'country_code': 'countryCode',
            'mcc': 'mcc',
            'terminal_id': 'terminalId',
            'amount': 'amount',
            'entry_mode': 'entryMode',
            'card': 'card',
            'cancelling_transaction_id': 'cancellingTransactionId'
        }
        self._transaction_id = transaction_id
        self._account_id = account_id
        self._transaction_date_time = transaction_date_time
        self._settlement_date_time = settlement_date_time
        self._transaction_type = transaction_type
        self._transaction_status = transaction_status
        self._transaction_authorization_response = transaction_authorization_response
        self._acquirer_id = acquirer_id
        self._acquirer_transaction_id = acquirer_transaction_id
        self._merchant_id = merchant_id
        self._merchant_name = merchant_name
        self._merchant_document_id = merchant_document_id
        self._merchant_address = merchant_address
        self._merchant_city = merchant_city
        self._merchant_uf = merchant_uf
        self._country_code = country_code
        self._mcc = mcc
        self._terminal_id = terminal_id
        self._amount = amount
        self._entry_mode = entry_mode
        self._card = card
        self._cancelling_transaction_id = cancelling_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'TransactionQueryResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransactionQueryResult of this TransactionQueryResult.  # noqa: E501
        :rtype: TransactionQueryResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_id(self) -> str:
        """Gets the transaction_id of this TransactionQueryResult.

        Identificador da transação atribuído pela paySmart.  # noqa: E501

        :return: The transaction_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        """Sets the transaction_id of this TransactionQueryResult.

        Identificador da transação atribuído pela paySmart.  # noqa: E501

        :param transaction_id: The transaction_id of this TransactionQueryResult.
        :type transaction_id: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def account_id(self) -> str:
        """Gets the account_id of this TransactionQueryResult.

        Identificador único da conta.  # noqa: E501

        :return: The account_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this TransactionQueryResult.

        Identificador único da conta.  # noqa: E501

        :param account_id: The account_id of this TransactionQueryResult.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def transaction_date_time(self) -> datetime:
        """Gets the transaction_date_time of this TransactionQueryResult.

        Data e hora da transação no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :return: The transaction_date_time of this TransactionQueryResult.
        :rtype: datetime
        """
        return self._transaction_date_time

    @transaction_date_time.setter
    def transaction_date_time(self, transaction_date_time: datetime):
        """Sets the transaction_date_time of this TransactionQueryResult.

        Data e hora da transação no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :param transaction_date_time: The transaction_date_time of this TransactionQueryResult.
        :type transaction_date_time: datetime
        """
        if transaction_date_time is None:
            raise ValueError("Invalid value for `transaction_date_time`, must not be `None`")  # noqa: E501

        self._transaction_date_time = transaction_date_time

    @property
    def settlement_date_time(self) -> datetime:
        """Gets the settlement_date_time of this TransactionQueryResult.

        Data e hora do recebimento na liquidação no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :return: The settlement_date_time of this TransactionQueryResult.
        :rtype: datetime
        """
        return self._settlement_date_time

    @settlement_date_time.setter
    def settlement_date_time(self, settlement_date_time: datetime):
        """Sets the settlement_date_time of this TransactionQueryResult.

        Data e hora do recebimento na liquidação no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :param settlement_date_time: The settlement_date_time of this TransactionQueryResult.
        :type settlement_date_time: datetime
        """

        self._settlement_date_time = settlement_date_time

    @property
    def transaction_type(self) -> TransactionType:
        """Gets the transaction_type of this TransactionQueryResult.


        :return: The transaction_type of this TransactionQueryResult.
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: TransactionType):
        """Sets the transaction_type of this TransactionQueryResult.


        :param transaction_type: The transaction_type of this TransactionQueryResult.
        :type transaction_type: TransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transaction_status(self) -> TransactionStatus:
        """Gets the transaction_status of this TransactionQueryResult.


        :return: The transaction_status of this TransactionQueryResult.
        :rtype: TransactionStatus
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status: TransactionStatus):
        """Sets the transaction_status of this TransactionQueryResult.


        :param transaction_status: The transaction_status of this TransactionQueryResult.
        :type transaction_status: TransactionStatus
        """
        if transaction_status is None:
            raise ValueError("Invalid value for `transaction_status`, must not be `None`")  # noqa: E501

        self._transaction_status = transaction_status

    @property
    def transaction_authorization_response(self) -> TransactionAuthorizationResponse:
        """Gets the transaction_authorization_response of this TransactionQueryResult.


        :return: The transaction_authorization_response of this TransactionQueryResult.
        :rtype: TransactionAuthorizationResponse
        """
        return self._transaction_authorization_response

    @transaction_authorization_response.setter
    def transaction_authorization_response(self, transaction_authorization_response: TransactionAuthorizationResponse):
        """Sets the transaction_authorization_response of this TransactionQueryResult.


        :param transaction_authorization_response: The transaction_authorization_response of this TransactionQueryResult.
        :type transaction_authorization_response: TransactionAuthorizationResponse
        """

        self._transaction_authorization_response = transaction_authorization_response

    @property
    def acquirer_id(self) -> str:
        """Gets the acquirer_id of this TransactionQueryResult.

        Código de identificação da rede de captura da transação.  # noqa: E501

        :return: The acquirer_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, acquirer_id: str):
        """Sets the acquirer_id of this TransactionQueryResult.

        Código de identificação da rede de captura da transação.  # noqa: E501

        :param acquirer_id: The acquirer_id of this TransactionQueryResult.
        :type acquirer_id: str
        """

        self._acquirer_id = acquirer_id

    @property
    def acquirer_transaction_id(self) -> str:
        """Gets the acquirer_transaction_id of this TransactionQueryResult.

        Identificador da transação na rede de captura.  # noqa: E501

        :return: The acquirer_transaction_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._acquirer_transaction_id

    @acquirer_transaction_id.setter
    def acquirer_transaction_id(self, acquirer_transaction_id: str):
        """Sets the acquirer_transaction_id of this TransactionQueryResult.

        Identificador da transação na rede de captura.  # noqa: E501

        :param acquirer_transaction_id: The acquirer_transaction_id of this TransactionQueryResult.
        :type acquirer_transaction_id: str
        """

        self._acquirer_transaction_id = acquirer_transaction_id

    @property
    def merchant_id(self) -> str:
        """Gets the merchant_id of this TransactionQueryResult.

        Identificação do estabelecimento informada na autorização.  # noqa: E501

        :return: The merchant_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id: str):
        """Sets the merchant_id of this TransactionQueryResult.

        Identificação do estabelecimento informada na autorização.  # noqa: E501

        :param merchant_id: The merchant_id of this TransactionQueryResult.
        :type merchant_id: str
        """

        self._merchant_id = merchant_id

    @property
    def merchant_name(self) -> str:
        """Gets the merchant_name of this TransactionQueryResult.

        Nome do estabelecimento.  # noqa: E501

        :return: The merchant_name of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name: str):
        """Sets the merchant_name of this TransactionQueryResult.

        Nome do estabelecimento.  # noqa: E501

        :param merchant_name: The merchant_name of this TransactionQueryResult.
        :type merchant_name: str
        """

        self._merchant_name = merchant_name

    @property
    def merchant_document_id(self) -> str:
        """Gets the merchant_document_id of this TransactionQueryResult.

        CNPJ do estabelecimento.  # noqa: E501

        :return: The merchant_document_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_document_id

    @merchant_document_id.setter
    def merchant_document_id(self, merchant_document_id: str):
        """Sets the merchant_document_id of this TransactionQueryResult.

        CNPJ do estabelecimento.  # noqa: E501

        :param merchant_document_id: The merchant_document_id of this TransactionQueryResult.
        :type merchant_document_id: str
        """

        self._merchant_document_id = merchant_document_id

    @property
    def merchant_address(self) -> str:
        """Gets the merchant_address of this TransactionQueryResult.

        Endereço do estabelecimento.  # noqa: E501

        :return: The merchant_address of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_address

    @merchant_address.setter
    def merchant_address(self, merchant_address: str):
        """Sets the merchant_address of this TransactionQueryResult.

        Endereço do estabelecimento.  # noqa: E501

        :param merchant_address: The merchant_address of this TransactionQueryResult.
        :type merchant_address: str
        """

        self._merchant_address = merchant_address

    @property
    def merchant_city(self) -> str:
        """Gets the merchant_city of this TransactionQueryResult.

        Cidade do estabelecimento.  # noqa: E501

        :return: The merchant_city of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_city

    @merchant_city.setter
    def merchant_city(self, merchant_city: str):
        """Sets the merchant_city of this TransactionQueryResult.

        Cidade do estabelecimento.  # noqa: E501

        :param merchant_city: The merchant_city of this TransactionQueryResult.
        :type merchant_city: str
        """

        self._merchant_city = merchant_city

    @property
    def merchant_uf(self) -> str:
        """Gets the merchant_uf of this TransactionQueryResult.

        Uf do estabelecimento  # noqa: E501

        :return: The merchant_uf of this TransactionQueryResult.
        :rtype: str
        """
        return self._merchant_uf

    @merchant_uf.setter
    def merchant_uf(self, merchant_uf: str):
        """Sets the merchant_uf of this TransactionQueryResult.

        Uf do estabelecimento  # noqa: E501

        :param merchant_uf: The merchant_uf of this TransactionQueryResult.
        :type merchant_uf: str
        """

        self._merchant_uf = merchant_uf

    @property
    def country_code(self) -> str:
        """Gets the country_code of this TransactionQueryResult.

        Código do país conforme ISO 3166-1.  # noqa: E501

        :return: The country_code of this TransactionQueryResult.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """Sets the country_code of this TransactionQueryResult.

        Código do país conforme ISO 3166-1.  # noqa: E501

        :param country_code: The country_code of this TransactionQueryResult.
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def mcc(self) -> str:
        """Gets the mcc of this TransactionQueryResult.

        MCC da transação  # noqa: E501

        :return: The mcc of this TransactionQueryResult.
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc: str):
        """Sets the mcc of this TransactionQueryResult.

        MCC da transação  # noqa: E501

        :param mcc: The mcc of this TransactionQueryResult.
        :type mcc: str
        """

        self._mcc = mcc

    @property
    def terminal_id(self) -> str:
        """Gets the terminal_id of this TransactionQueryResult.

        Identificação do terminal informada na autorização.  # noqa: E501

        :return: The terminal_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id: str):
        """Sets the terminal_id of this TransactionQueryResult.

        Identificação do terminal informada na autorização.  # noqa: E501

        :param terminal_id: The terminal_id of this TransactionQueryResult.
        :type terminal_id: str
        """

        self._terminal_id = terminal_id

    @property
    def amount(self) -> Amount:
        """Gets the amount of this TransactionQueryResult.


        :return: The amount of this TransactionQueryResult.
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount: Amount):
        """Sets the amount of this TransactionQueryResult.


        :param amount: The amount of this TransactionQueryResult.
        :type amount: Amount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def entry_mode(self) -> EntryMode:
        """Gets the entry_mode of this TransactionQueryResult.


        :return: The entry_mode of this TransactionQueryResult.
        :rtype: EntryMode
        """
        return self._entry_mode

    @entry_mode.setter
    def entry_mode(self, entry_mode: EntryMode):
        """Sets the entry_mode of this TransactionQueryResult.


        :param entry_mode: The entry_mode of this TransactionQueryResult.
        :type entry_mode: EntryMode
        """

        self._entry_mode = entry_mode

    @property
    def card(self) -> AllOfTransactionQueryResultCard:
        """Gets the card of this TransactionQueryResult.

        Se transação foi realizada por meio de um cartão, os dados do cartão são representados por este campo.  # noqa: E501

        :return: The card of this TransactionQueryResult.
        :rtype: AllOfTransactionQueryResultCard
        """
        return self._card

    @card.setter
    def card(self, card: AllOfTransactionQueryResultCard):
        """Sets the card of this TransactionQueryResult.

        Se transação foi realizada por meio de um cartão, os dados do cartão são representados por este campo.  # noqa: E501

        :param card: The card of this TransactionQueryResult.
        :type card: AllOfTransactionQueryResultCard
        """

        self._card = card

    @property
    def cancelling_transaction_id(self) -> str:
        """Gets the cancelling_transaction_id of this TransactionQueryResult.

        Identificador da transação que realizou o estorno dessa transação.  # noqa: E501

        :return: The cancelling_transaction_id of this TransactionQueryResult.
        :rtype: str
        """
        return self._cancelling_transaction_id

    @cancelling_transaction_id.setter
    def cancelling_transaction_id(self, cancelling_transaction_id: str):
        """Sets the cancelling_transaction_id of this TransactionQueryResult.

        Identificador da transação que realizou o estorno dessa transação.  # noqa: E501

        :param cancelling_transaction_id: The cancelling_transaction_id of this TransactionQueryResult.
        :type cancelling_transaction_id: str
        """

        self._cancelling_transaction_id = cancelling_transaction_id
