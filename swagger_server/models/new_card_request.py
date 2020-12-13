# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server import util


class NewCardRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, issuer_request_id: str=None, issuer_card_id: str=None, delivery_kit_code: float=None, extra_data: str=None, inhibit_physical_card: bool=None, new_pin: AllOfNewCardRequestNewPin=None, cardholder: AllOfNewCardRequestCardholder=None, card_delivery_address: AllOfNewCardRequestCardDeliveryAddress=None, source_audit: SourceAudit=None):  # noqa: E501
        """NewCardRequest - a model defined in Swagger

        :param issuer_request_id: The issuer_request_id of this NewCardRequest.  # noqa: E501
        :type issuer_request_id: str
        :param issuer_card_id: The issuer_card_id of this NewCardRequest.  # noqa: E501
        :type issuer_card_id: str
        :param delivery_kit_code: The delivery_kit_code of this NewCardRequest.  # noqa: E501
        :type delivery_kit_code: float
        :param extra_data: The extra_data of this NewCardRequest.  # noqa: E501
        :type extra_data: str
        :param inhibit_physical_card: The inhibit_physical_card of this NewCardRequest.  # noqa: E501
        :type inhibit_physical_card: bool
        :param new_pin: The new_pin of this NewCardRequest.  # noqa: E501
        :type new_pin: AllOfNewCardRequestNewPin
        :param cardholder: The cardholder of this NewCardRequest.  # noqa: E501
        :type cardholder: AllOfNewCardRequestCardholder
        :param card_delivery_address: The card_delivery_address of this NewCardRequest.  # noqa: E501
        :type card_delivery_address: AllOfNewCardRequestCardDeliveryAddress
        :param source_audit: The source_audit of this NewCardRequest.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'issuer_request_id': str,
            'issuer_card_id': str,
            'delivery_kit_code': float,
            'extra_data': str,
            'inhibit_physical_card': bool,
            'new_pin': AllOfNewCardRequestNewPin,
            'cardholder': AllOfNewCardRequestCardholder,
            'card_delivery_address': AllOfNewCardRequestCardDeliveryAddress,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'issuer_request_id': 'issuerRequestId',
            'issuer_card_id': 'issuerCardId',
            'delivery_kit_code': 'deliveryKitCode',
            'extra_data': 'extraData',
            'inhibit_physical_card': 'inhibitPhysicalCard',
            'new_pin': 'newPin',
            'cardholder': 'cardholder',
            'card_delivery_address': 'cardDeliveryAddress',
            'source_audit': 'sourceAudit'
        }
        self._issuer_request_id = issuer_request_id
        self._issuer_card_id = issuer_card_id
        self._delivery_kit_code = delivery_kit_code
        self._extra_data = extra_data
        self._inhibit_physical_card = inhibit_physical_card
        self._new_pin = new_pin
        self._cardholder = cardholder
        self._card_delivery_address = card_delivery_address
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'NewCardRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewCardRequest of this NewCardRequest.  # noqa: E501
        :rtype: NewCardRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issuer_request_id(self) -> str:
        """Gets the issuer_request_id of this NewCardRequest.

        Identificador único da requisição gerado pelo emissor. Esse identificador é ecoado na resposta. Nenhuma verificação dele é feita por parte da paySmart, o emissor é livre para escolher o valor que quiser.  # noqa: E501

        :return: The issuer_request_id of this NewCardRequest.
        :rtype: str
        """
        return self._issuer_request_id

    @issuer_request_id.setter
    def issuer_request_id(self, issuer_request_id: str):
        """Sets the issuer_request_id of this NewCardRequest.

        Identificador único da requisição gerado pelo emissor. Esse identificador é ecoado na resposta. Nenhuma verificação dele é feita por parte da paySmart, o emissor é livre para escolher o valor que quiser.  # noqa: E501

        :param issuer_request_id: The issuer_request_id of this NewCardRequest.
        :type issuer_request_id: str
        """

        self._issuer_request_id = issuer_request_id

    @property
    def issuer_card_id(self) -> str:
        """Gets the issuer_card_id of this NewCardRequest.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :return: The issuer_card_id of this NewCardRequest.
        :rtype: str
        """
        return self._issuer_card_id

    @issuer_card_id.setter
    def issuer_card_id(self, issuer_card_id: str):
        """Sets the issuer_card_id of this NewCardRequest.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :param issuer_card_id: The issuer_card_id of this NewCardRequest.
        :type issuer_card_id: str
        """

        self._issuer_card_id = issuer_card_id

    @property
    def delivery_kit_code(self) -> float:
        """Gets the delivery_kit_code of this NewCardRequest.

        Código numérico de seis dígitos combinado entre emissor, paySmart e gráfica, para determinar a arte do cartão.  # noqa: E501

        :return: The delivery_kit_code of this NewCardRequest.
        :rtype: float
        """
        return self._delivery_kit_code

    @delivery_kit_code.setter
    def delivery_kit_code(self, delivery_kit_code: float):
        """Sets the delivery_kit_code of this NewCardRequest.

        Código numérico de seis dígitos combinado entre emissor, paySmart e gráfica, para determinar a arte do cartão.  # noqa: E501

        :param delivery_kit_code: The delivery_kit_code of this NewCardRequest.
        :type delivery_kit_code: float
        """

        self._delivery_kit_code = delivery_kit_code

    @property
    def extra_data(self) -> str:
        """Gets the extra_data of this NewCardRequest.

        Campo livre que pode assumir o significado desejado pelo emissor, conforme combinação prévia com paySmart e gráfica (exexmplo - código de barras, recebimento de lotes, etc.)  # noqa: E501

        :return: The extra_data of this NewCardRequest.
        :rtype: str
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data: str):
        """Sets the extra_data of this NewCardRequest.

        Campo livre que pode assumir o significado desejado pelo emissor, conforme combinação prévia com paySmart e gráfica (exexmplo - código de barras, recebimento de lotes, etc.)  # noqa: E501

        :param extra_data: The extra_data of this NewCardRequest.
        :type extra_data: str
        """

        self._extra_data = extra_data

    @property
    def inhibit_physical_card(self) -> bool:
        """Gets the inhibit_physical_card of this NewCardRequest.

        Flag indicando que o cartão físico não deve ser impresso. O valor padrão é \"false\", ou seja, o cartão será enviado normalmente para a gráfica  # noqa: E501

        :return: The inhibit_physical_card of this NewCardRequest.
        :rtype: bool
        """
        return self._inhibit_physical_card

    @inhibit_physical_card.setter
    def inhibit_physical_card(self, inhibit_physical_card: bool):
        """Sets the inhibit_physical_card of this NewCardRequest.

        Flag indicando que o cartão físico não deve ser impresso. O valor padrão é \"false\", ou seja, o cartão será enviado normalmente para a gráfica  # noqa: E501

        :param inhibit_physical_card: The inhibit_physical_card of this NewCardRequest.
        :type inhibit_physical_card: bool
        """

        self._inhibit_physical_card = inhibit_physical_card

    @property
    def new_pin(self) -> AllOfNewCardRequestNewPin:
        """Gets the new_pin of this NewCardRequest.

        Senha que deve ser atribuída ao cartão  # noqa: E501

        :return: The new_pin of this NewCardRequest.
        :rtype: AllOfNewCardRequestNewPin
        """
        return self._new_pin

    @new_pin.setter
    def new_pin(self, new_pin: AllOfNewCardRequestNewPin):
        """Sets the new_pin of this NewCardRequest.

        Senha que deve ser atribuída ao cartão  # noqa: E501

        :param new_pin: The new_pin of this NewCardRequest.
        :type new_pin: AllOfNewCardRequestNewPin
        """

        self._new_pin = new_pin

    @property
    def cardholder(self) -> AllOfNewCardRequestCardholder:
        """Gets the cardholder of this NewCardRequest.

        Informações relacionadas ao portador do cartão.  Obrigatório caso não se trate de um cartão anônimo vinculado a uma conta.  # noqa: E501

        :return: The cardholder of this NewCardRequest.
        :rtype: AllOfNewCardRequestCardholder
        """
        return self._cardholder

    @cardholder.setter
    def cardholder(self, cardholder: AllOfNewCardRequestCardholder):
        """Sets the cardholder of this NewCardRequest.

        Informações relacionadas ao portador do cartão.  Obrigatório caso não se trate de um cartão anônimo vinculado a uma conta.  # noqa: E501

        :param cardholder: The cardholder of this NewCardRequest.
        :type cardholder: AllOfNewCardRequestCardholder
        """

        self._cardholder = cardholder

    @property
    def card_delivery_address(self) -> AllOfNewCardRequestCardDeliveryAddress:
        """Gets the card_delivery_address of this NewCardRequest.

        Endereço para entrega do cartão. Opcional, se não for enviado é usado o endereço definido para a conta.  # noqa: E501

        :return: The card_delivery_address of this NewCardRequest.
        :rtype: AllOfNewCardRequestCardDeliveryAddress
        """
        return self._card_delivery_address

    @card_delivery_address.setter
    def card_delivery_address(self, card_delivery_address: AllOfNewCardRequestCardDeliveryAddress):
        """Sets the card_delivery_address of this NewCardRequest.

        Endereço para entrega do cartão. Opcional, se não for enviado é usado o endereço definido para a conta.  # noqa: E501

        :param card_delivery_address: The card_delivery_address of this NewCardRequest.
        :type card_delivery_address: AllOfNewCardRequestCardDeliveryAddress
        """

        self._card_delivery_address = card_delivery_address

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this NewCardRequest.


        :return: The source_audit of this NewCardRequest.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this NewCardRequest.


        :param source_audit: The source_audit of this NewCardRequest.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit
