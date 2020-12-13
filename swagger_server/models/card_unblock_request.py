# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server import util


class CardUnblockRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, issuer_card_unblock_id: str=None, unblock_code: int=None, reason: str=None, source_audit: SourceAudit=None):  # noqa: E501
        """CardUnblockRequest - a model defined in Swagger

        :param issuer_card_unblock_id: The issuer_card_unblock_id of this CardUnblockRequest.  # noqa: E501
        :type issuer_card_unblock_id: str
        :param unblock_code: The unblock_code of this CardUnblockRequest.  # noqa: E501
        :type unblock_code: int
        :param reason: The reason of this CardUnblockRequest.  # noqa: E501
        :type reason: str
        :param source_audit: The source_audit of this CardUnblockRequest.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'issuer_card_unblock_id': str,
            'unblock_code': int,
            'reason': str,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'issuer_card_unblock_id': 'issuerCardUnblockId',
            'unblock_code': 'unblockCode',
            'reason': 'reason',
            'source_audit': 'sourceAudit'
        }
        self._issuer_card_unblock_id = issuer_card_unblock_id
        self._unblock_code = unblock_code
        self._reason = reason
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'CardUnblockRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardUnblockRequest of this CardUnblockRequest.  # noqa: E501
        :rtype: CardUnblockRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issuer_card_unblock_id(self) -> str:
        """Gets the issuer_card_unblock_id of this CardUnblockRequest.

        Identificador único da requisição de desbloqueio. Gerado pelo emissor.  # noqa: E501

        :return: The issuer_card_unblock_id of this CardUnblockRequest.
        :rtype: str
        """
        return self._issuer_card_unblock_id

    @issuer_card_unblock_id.setter
    def issuer_card_unblock_id(self, issuer_card_unblock_id: str):
        """Sets the issuer_card_unblock_id of this CardUnblockRequest.

        Identificador único da requisição de desbloqueio. Gerado pelo emissor.  # noqa: E501

        :param issuer_card_unblock_id: The issuer_card_unblock_id of this CardUnblockRequest.
        :type issuer_card_unblock_id: str
        """

        self._issuer_card_unblock_id = issuer_card_unblock_id

    @property
    def unblock_code(self) -> int:
        """Gets the unblock_code of this CardUnblockRequest.

        Código identificando o tipo de desbloqueio.  # noqa: E501

        :return: The unblock_code of this CardUnblockRequest.
        :rtype: int
        """
        return self._unblock_code

    @unblock_code.setter
    def unblock_code(self, unblock_code: int):
        """Sets the unblock_code of this CardUnblockRequest.

        Código identificando o tipo de desbloqueio.  # noqa: E501

        :param unblock_code: The unblock_code of this CardUnblockRequest.
        :type unblock_code: int
        """
        if unblock_code is None:
            raise ValueError("Invalid value for `unblock_code`, must not be `None`")  # noqa: E501

        self._unblock_code = unblock_code

    @property
    def reason(self) -> str:
        """Gets the reason of this CardUnblockRequest.

        Motivo do desbloqueio.  # noqa: E501

        :return: The reason of this CardUnblockRequest.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this CardUnblockRequest.

        Motivo do desbloqueio.  # noqa: E501

        :param reason: The reason of this CardUnblockRequest.
        :type reason: str
        """

        self._reason = reason

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this CardUnblockRequest.


        :return: The source_audit of this CardUnblockRequest.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this CardUnblockRequest.


        :param source_audit: The source_audit of this CardUnblockRequest.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit
