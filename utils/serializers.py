from typing import Tuple

from rest_framework.serializers import ModelSerializer

from modules.core.models.base import ModelBase


class BaseModelSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", ())
        exclude = kwargs.pop("exclude", ())

        super().__init__(*args, **kwargs)

        self._existing_fields = set(self.fields.keys())

        self.apply_fields(fields)
        self.apply_exclude(exclude)
    
    def __new__(cls, *args, **kwargs):
        print(cls, *args, **kwargs)
        print(A)
        # setattr(cls.Meta, "model", )

    @classmethod
    def _many_init(cls, *args, **kwargs):
        

    def apply_fields(self, fields: Tuple[str, ...] = ()):
        if fields:
            _trash = self._existing_fields.difference(fields)
            for field in _trash:
                self.fields.pop(field)

    def apply_exclude(self, exclude: Tuple[str, ...] = ()):
        if exclude:
            _trash = self._existing_fields.difference(exclude)
            for field in self._existing_fields:
                self.fields.pop(
                    field
                ) if field in ModelBase.BASE_MODEL_FIELDS_EXCEPT_UUID or field in _trash else None

    @property
    def dict_data(self) -> dict:
        return super().data
