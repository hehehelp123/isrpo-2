import connexion
import six

from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def models_get():  # noqa: E501
    """Получить список всех моделей

     # noqa: E501


    :rtype: List[Model]
    """
    return 'do some magic!'


def models_model_id_delete(model_id):  # noqa: E501
    """Удалить модель

     # noqa: E501

    :param model_id: 
    :type model_id: str

    :rtype: None
    """
    return 'do some magic!'


def models_model_id_get(model_id):  # noqa: E501
    """Получить информацию о модели

     # noqa: E501

    :param model_id: 
    :type model_id: str

    :rtype: Model
    """
    return 'do some magic!'


def models_model_id_put(body, model_id):  # noqa: E501
    """Обновить информацию о модели

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param model_id: 
    :type model_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def models_post(body):  # noqa: E501
    """Добавить новую модель

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Model.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_login_post(body):  # noqa: E501
    """Войти в систему

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Token
    """
    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Зарегистрировать нового пользователя

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
