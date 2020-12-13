# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_owner_data import AccountOwnerData  # noqa: F401,E501
from swagger_server.models.contact_information import ContactInformation  # noqa: F401,E501
from swagger_server.models.occupation_info import OccupationInfo  # noqa: F401,E501
from swagger_server.models.personal_identity_document_info import PersonalIdentityDocumentInfo  # noqa: F401,E501
from swagger_server import util


class AllOfAccountAccountOwner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, full_name: str=None, identity_document_number: str=None, other_identity_document_number: PersonalIdentityDocumentInfo=None, mother_name: str=None, contact_information: ContactInformation=None, occupation_info: OccupationInfo=None):  # noqa: E501
        """AllOfAccountAccountOwner - a model defined in Swagger

        :param full_name: The full_name of this AllOfAccountAccountOwner.  # noqa: E501
        :type full_name: str
        :param identity_document_number: The identity_document_number of this AllOfAccountAccountOwner.  # noqa: E501
        :type identity_document_number: str
        :param other_identity_document_number: The other_identity_document_number of this AllOfAccountAccountOwner.  # noqa: E501
        :type other_identity_document_number: PersonalIdentityDocumentInfo
        :param mother_name: The mother_name of this AllOfAccountAccountOwner.  # noqa: E501
        :type mother_name: str
        :param contact_information: The contact_information of this AllOfAccountAccountOwner.  # noqa: E501
        :type contact_information: ContactInformation
        :param occupation_info: The occupation_info of this AllOfAccountAccountOwner.  # noqa: E501
        :type occupation_info: OccupationInfo
        """
        self.swagger_types = {
            'full_name': str,
            'identity_document_number': str,
            'other_identity_document_number': PersonalIdentityDocumentInfo,
            'mother_name': str,
            'contact_information': ContactInformation,
            'occupation_info': OccupationInfo
        }

        self.attribute_map = {
            'full_name': 'fullName',
            'identity_document_number': 'identityDocumentNumber',
            'other_identity_document_number': 'otherIdentityDocumentNumber',
            'mother_name': 'motherName',
            'contact_information': 'contactInformation',
            'occupation_info': 'occupationInfo'
        }
        self._full_name = full_name
        self._identity_document_number = identity_document_number
        self._other_identity_document_number = other_identity_document_number
        self._mother_name = mother_name
        self._contact_information = contact_information
        self._occupation_info = occupation_info

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfAccountAccountOwner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfAccountAccountOwner of this AllOfAccountAccountOwner.  # noqa: E501
        :rtype: AllOfAccountAccountOwner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def full_name(self) -> str:
        """Gets the full_name of this AllOfAccountAccountOwner.

        Nome completo do portador, ou razão social se for pessoa jurídica.  # noqa: E501

        :return: The full_name of this AllOfAccountAccountOwner.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        """Sets the full_name of this AllOfAccountAccountOwner.

        Nome completo do portador, ou razão social se for pessoa jurídica.  # noqa: E501

        :param full_name: The full_name of this AllOfAccountAccountOwner.
        :type full_name: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def identity_document_number(self) -> str:
        """Gets the identity_document_number of this AllOfAccountAccountOwner.

        No Brasil, usar CPF ou CNPJ do portador.  # noqa: E501

        :return: The identity_document_number of this AllOfAccountAccountOwner.
        :rtype: str
        """
        return self._identity_document_number

    @identity_document_number.setter
    def identity_document_number(self, identity_document_number: str):
        """Sets the identity_document_number of this AllOfAccountAccountOwner.

        No Brasil, usar CPF ou CNPJ do portador.  # noqa: E501

        :param identity_document_number: The identity_document_number of this AllOfAccountAccountOwner.
        :type identity_document_number: str
        """
        if identity_document_number is None:
            raise ValueError("Invalid value for `identity_document_number`, must not be `None`")  # noqa: E501

        self._identity_document_number = identity_document_number

    @property
    def other_identity_document_number(self) -> PersonalIdentityDocumentInfo:
        """Gets the other_identity_document_number of this AllOfAccountAccountOwner.


        :return: The other_identity_document_number of this AllOfAccountAccountOwner.
        :rtype: PersonalIdentityDocumentInfo
        """
        return self._other_identity_document_number

    @other_identity_document_number.setter
    def other_identity_document_number(self, other_identity_document_number: PersonalIdentityDocumentInfo):
        """Sets the other_identity_document_number of this AllOfAccountAccountOwner.


        :param other_identity_document_number: The other_identity_document_number of this AllOfAccountAccountOwner.
        :type other_identity_document_number: PersonalIdentityDocumentInfo
        """

        self._other_identity_document_number = other_identity_document_number

    @property
    def mother_name(self) -> str:
        """Gets the mother_name of this AllOfAccountAccountOwner.

        Nome completo da mãe do titular.  # noqa: E501

        :return: The mother_name of this AllOfAccountAccountOwner.
        :rtype: str
        """
        return self._mother_name

    @mother_name.setter
    def mother_name(self, mother_name: str):
        """Sets the mother_name of this AllOfAccountAccountOwner.

        Nome completo da mãe do titular.  # noqa: E501

        :param mother_name: The mother_name of this AllOfAccountAccountOwner.
        :type mother_name: str
        """

        self._mother_name = mother_name

    @property
    def contact_information(self) -> ContactInformation:
        """Gets the contact_information of this AllOfAccountAccountOwner.


        :return: The contact_information of this AllOfAccountAccountOwner.
        :rtype: ContactInformation
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information: ContactInformation):
        """Sets the contact_information of this AllOfAccountAccountOwner.


        :param contact_information: The contact_information of this AllOfAccountAccountOwner.
        :type contact_information: ContactInformation
        """
        if contact_information is None:
            raise ValueError("Invalid value for `contact_information`, must not be `None`")  # noqa: E501

        self._contact_information = contact_information

    @property
    def occupation_info(self) -> OccupationInfo:
        """Gets the occupation_info of this AllOfAccountAccountOwner.


        :return: The occupation_info of this AllOfAccountAccountOwner.
        :rtype: OccupationInfo
        """
        return self._occupation_info

    @occupation_info.setter
    def occupation_info(self, occupation_info: OccupationInfo):
        """Sets the occupation_info of this AllOfAccountAccountOwner.


        :param occupation_info: The occupation_info of this AllOfAccountAccountOwner.
        :type occupation_info: OccupationInfo
        """

        self._occupation_info = occupation_info
