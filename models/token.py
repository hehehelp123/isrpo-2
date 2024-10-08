# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Token(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, access_token: str=None, token_type: str=None):  # noqa: E501
        """Token - a model defined in Swagger

        :param access_token: The access_token of this Token.  # noqa: E501
        :type access_token: str
        :param token_type: The token_type of this Token.  # noqa: E501
        :type token_type: str
        """
        self.swagger_types = {
            'access_token': str,
            'token_type': str
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'token_type': 'token_type'
        }
        self._access_token = access_token
        self._token_type = token_type

    @classmethod
    def from_dict(cls, dikt) -> 'Token':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Token of this Token.  # noqa: E501
        :rtype: Token
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self) -> str:
        """Gets the access_token of this Token.

        Токен доступа  # noqa: E501

        :return: The access_token of this Token.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token: str):
        """Sets the access_token of this Token.

        Токен доступа  # noqa: E501

        :param access_token: The access_token of this Token.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def token_type(self) -> str:
        """Gets the token_type of this Token.

        Тип токена (например, Bearer)  # noqa: E501

        :return: The token_type of this Token.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type: str):
        """Sets the token_type of this Token.

        Тип токена (например, Bearer)  # noqa: E501

        :param token_type: The token_type of this Token.
        :type token_type: str
        """

        self._token_type = token_type
