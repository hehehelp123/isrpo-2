# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_models_get(self):
        """Test case for models_get

        Получить список всех моделей
        """
        response = self.client.open(
            '/models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_models_model_id_delete(self):
        """Test case for models_model_id_delete

        Удалить модель
        """
        response = self.client.open(
            '/models/{modelId}'.format(model_id='model_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_models_model_id_get(self):
        """Test case for models_model_id_get

        Получить информацию о модели
        """
        response = self.client.open(
            '/models/{modelId}'.format(model_id='model_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_models_model_id_put(self):
        """Test case for models_model_id_put

        Обновить информацию о модели
        """
        body = Model()
        response = self.client.open(
            '/models/{modelId}'.format(model_id='model_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_models_post(self):
        """Test case for models_post

        Добавить новую модель
        """
        body = Model()
        response = self.client.open(
            '/models',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_login_post(self):
        """Test case for users_login_post

        Войти в систему
        """
        body = Login()
        response = self.client.open(
            '/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Зарегистрировать нового пользователя
        """
        body = User()
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
