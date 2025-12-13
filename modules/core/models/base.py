import uuid6
from django.db import models

from modules.core.choices import StatusChoices
from modules.core.managers import DeleteStatusManager


class ModelBase(models.Model):
    BASE_MODEL_HIDDEN_FIELDS = (
        "id",
        "status",
    )
    BASE_MODEL_TIME_FIELDS = (
        "created_at",
        "updated_at",
    )
    BASE_MODEL_FIELDS_EXCEPT_UUID = BASE_MODEL_HIDDEN_FIELDS + BASE_MODEL_TIME_FIELDS
    BASE_MODEL_FIELDS = BASE_MODEL_FIELDS_EXCEPT_UUID + ("uuid",)

    uuid = models.UUIDField(default=uuid6.uuid6, unique=True)
    status = models.IntegerField(choices=StatusChoices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DeleteStatusManager()

    class Meta:
        abstract = True


class Dropdown(models.Model):
    label = models.TextField()
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, related_name="children"
    )
