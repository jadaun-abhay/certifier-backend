from modules.core.api.v1.serializers import UserSerializer
from utils.types import BaseRequest
from utils.views import BaseAPIView


class RegistrationView(BaseAPIView):
    def post(self, request: BaseRequest):
        data = request.data

        body_srlz = UserSerializer(data=data)
        body_srlz.is_valid(raise_exception=True)

        user_service = UserService.create_user(**body_srlz.dict_data)
