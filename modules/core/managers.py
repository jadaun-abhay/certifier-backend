from django.db import models

from modules.core.choices import StatusChoices


class DeleteStatusManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().exclude(status=StatusChoices.DELETE)
