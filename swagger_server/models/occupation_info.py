# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class OccupationInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, company_name: str=None, job_title: str=None, current_job_time: int=None, income: AllOfOccupationInfoIncome=None, income_range: str=None):  # noqa: E501
        """OccupationInfo - a model defined in Swagger

        :param company_name: The company_name of this OccupationInfo.  # noqa: E501
        :type company_name: str
        :param job_title: The job_title of this OccupationInfo.  # noqa: E501
        :type job_title: str
        :param current_job_time: The current_job_time of this OccupationInfo.  # noqa: E501
        :type current_job_time: int
        :param income: The income of this OccupationInfo.  # noqa: E501
        :type income: AllOfOccupationInfoIncome
        :param income_range: The income_range of this OccupationInfo.  # noqa: E501
        :type income_range: str
        """
        self.swagger_types = {
            'company_name': str,
            'job_title': str,
            'current_job_time': int,
            'income': AllOfOccupationInfoIncome,
            'income_range': str
        }

        self.attribute_map = {
            'company_name': 'companyName',
            'job_title': 'jobTitle',
            'current_job_time': 'currentJobTime',
            'income': 'income',
            'income_range': 'incomeRange'
        }
        self._company_name = company_name
        self._job_title = job_title
        self._current_job_time = current_job_time
        self._income = income
        self._income_range = income_range

    @classmethod
    def from_dict(cls, dikt) -> 'OccupationInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OccupationInfo of this OccupationInfo.  # noqa: E501
        :rtype: OccupationInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_name(self) -> str:
        """Gets the company_name of this OccupationInfo.

        Nome da empresa onde trabalha  # noqa: E501

        :return: The company_name of this OccupationInfo.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        """Sets the company_name of this OccupationInfo.

        Nome da empresa onde trabalha  # noqa: E501

        :param company_name: The company_name of this OccupationInfo.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def job_title(self) -> str:
        """Gets the job_title of this OccupationInfo.

        Nome do cargo ou função exercida na empresa.  # noqa: E501

        :return: The job_title of this OccupationInfo.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title: str):
        """Sets the job_title of this OccupationInfo.

        Nome do cargo ou função exercida na empresa.  # noqa: E501

        :param job_title: The job_title of this OccupationInfo.
        :type job_title: str
        """

        self._job_title = job_title

    @property
    def current_job_time(self) -> int:
        """Gets the current_job_time of this OccupationInfo.

        Quantos anos no cargo atual.  # noqa: E501

        :return: The current_job_time of this OccupationInfo.
        :rtype: int
        """
        return self._current_job_time

    @current_job_time.setter
    def current_job_time(self, current_job_time: int):
        """Sets the current_job_time of this OccupationInfo.

        Quantos anos no cargo atual.  # noqa: E501

        :param current_job_time: The current_job_time of this OccupationInfo.
        :type current_job_time: int
        """

        self._current_job_time = current_job_time

    @property
    def income(self) -> AllOfOccupationInfoIncome:
        """Gets the income of this OccupationInfo.

        Salário ou renda da pessoa.  # noqa: E501

        :return: The income of this OccupationInfo.
        :rtype: AllOfOccupationInfoIncome
        """
        return self._income

    @income.setter
    def income(self, income: AllOfOccupationInfoIncome):
        """Sets the income of this OccupationInfo.

        Salário ou renda da pessoa.  # noqa: E501

        :param income: The income of this OccupationInfo.
        :type income: AllOfOccupationInfoIncome
        """

        self._income = income

    @property
    def income_range(self) -> str:
        """Gets the income_range of this OccupationInfo.

        Faixa salarial ou de renda. * 01 - Até R$ 1500,00. * 02 - R$ 1500,01 a R$ 3000,00. * 03 - R$ 3000,01 a R$ 5000,00. * 04 - R$ 5000,01 a R$ 8000,00. * 05 - Acima de R$ 8000,01.  # noqa: E501

        :return: The income_range of this OccupationInfo.
        :rtype: str
        """
        return self._income_range

    @income_range.setter
    def income_range(self, income_range: str):
        """Sets the income_range of this OccupationInfo.

        Faixa salarial ou de renda. * 01 - Até R$ 1500,00. * 02 - R$ 1500,01 a R$ 3000,00. * 03 - R$ 3000,01 a R$ 5000,00. * 04 - R$ 5000,01 a R$ 8000,00. * 05 - Acima de R$ 8000,01.  # noqa: E501

        :param income_range: The income_range of this OccupationInfo.
        :type income_range: str
        """

        self._income_range = income_range
