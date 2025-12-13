from django.db import models


class StatusChoices(models.IntegerChoices):
    DELETE = 0, "DELETED"
    CREATE = 1, "CREATED"
    UPDATE = 2, "UPDATED"


class FileTypeChoices(models.IntegerChoices):
    PROFILE = 0
    GENERAL = 1
