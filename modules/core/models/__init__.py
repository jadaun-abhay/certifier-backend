from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from modules.core.choices import FileTypeChoices
from modules.core.models.base import Dropdown, ModelBase

__all__ = ["Dropdown"]


class User(AbstractUser, ModelBase):
    username = None
    middle_name = models.CharField(max_length=60, blank=True)
    phone_number = models.PositiveBigIntegerField(blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class UploadFile(ModelBase):
    type = models.IntegerField(choices=FileTypeChoices)
    file = models.FileField()
