from modules.core.models import User
from utils.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        exclude = User.BASE_MODEL_FIELDS_EXCEPT_UUID
