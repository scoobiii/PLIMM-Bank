# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server import util


class CancelVirtualCardRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, issuer_request_id: str=None, cancellation_code: int=None, reason: str=None, source_audit: SourceAudit=None):  # noqa: E501
        """CancelVirtualCardRequest - a model defined in Swagger

        :param issuer_request_id: The issuer_request_id of this CancelVirtualCardRequest.  # noqa: E501
        :type issuer_request_id: str
        :param cancellation_code: The cancellation_code of this CancelVirtualCardRequest.  # noqa: E501
        :type cancellation_code: int
        :param reason: The reason of this CancelVirtualCardRequest.  # noqa: E501
        :type reason: str
        :param source_audit: The source_audit of this CancelVirtualCardRequest.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'issuer_request_id': str,
            'cancellation_code': int,
            'reason': str,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'issuer_request_id': 'issuerRequestId',
            'cancellation_code': 'cancellationCode',
            'reason': 'reason',
            'source_audit': 'sourceAudit'
        }
        self._issuer_request_id = issuer_request_id
        self._cancellation_code = cancellation_code
        self._reason = reason
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'CancelVirtualCardRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CancelVirtualCardRequest of this CancelVirtualCardRequest.  # noqa: E501
        :rtype: CancelVirtualCardRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issuer_request_id(self) -> str:
        """Gets the issuer_request_id of this CancelVirtualCardRequest.

        Identificador único da requisição gerado pelo emissor. Esse identificador é ecoado na resposta. Nenhuma verificação dele é feita por parte da paySmart, o emissor é livre para escolher o valor que quiser.  # noqa: E501

        :return: The issuer_request_id of this CancelVirtualCardRequest.
        :rtype: str
        """
        return self._issuer_request_id

    @issuer_request_id.setter
    def issuer_request_id(self, issuer_request_id: str):
        """Sets the issuer_request_id of this CancelVirtualCardRequest.

        Identificador único da requisição gerado pelo emissor. Esse identificador é ecoado na resposta. Nenhuma verificação dele é feita por parte da paySmart, o emissor é livre para escolher o valor que quiser.  # noqa: E501

        :param issuer_request_id: The issuer_request_id of this CancelVirtualCardRequest.
        :type issuer_request_id: str
        """

        self._issuer_request_id = issuer_request_id

    @property
    def cancellation_code(self) -> int:
        """Gets the cancellation_code of this CancelVirtualCardRequest.

        Código identificando o tipo de cancelamento.  # noqa: E501

        :return: The cancellation_code of this CancelVirtualCardRequest.
        :rtype: int
        """
        return self._cancellation_code

    @cancellation_code.setter
    def cancellation_code(self, cancellation_code: int):
        """Sets the cancellation_code of this CancelVirtualCardRequest.

        Código identificando o tipo de cancelamento.  # noqa: E501

        :param cancellation_code: The cancellation_code of this CancelVirtualCardRequest.
        :type cancellation_code: int
        """
        if cancellation_code is None:
            raise ValueError("Invalid value for `cancellation_code`, must not be `None`")  # noqa: E501

        self._cancellation_code = cancellation_code

    @property
    def reason(self) -> str:
        """Gets the reason of this CancelVirtualCardRequest.

        Motivo do cancelamento.  # noqa: E501

        :return: The reason of this CancelVirtualCardRequest.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this CancelVirtualCardRequest.

        Motivo do cancelamento.  # noqa: E501

        :param reason: The reason of this CancelVirtualCardRequest.
        :type reason: str
        """

        self._reason = reason

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this CancelVirtualCardRequest.


        :return: The source_audit of this CancelVirtualCardRequest.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this CancelVirtualCardRequest.


        :param source_audit: The source_audit of this CancelVirtualCardRequest.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit
