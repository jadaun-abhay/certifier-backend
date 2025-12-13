from rest_framework.request import Request

from modules.core.models import User


class BaseRequest(Request):
    user: User
