from rest_framework.views import APIView
from apps.users.requests.create_user_request import CreateUserRequest
from apps.users.services.user_service import UserService
from apps.core.constants.messages import Messages
from apps.core.constants.status_codes import StatusCodes
from apps.core.utils.api_response import api_response

class UserCreateController(APIView):

    def post(self, request):
        try:        
            req = CreateUserRequest(data=request.data)
            req.is_valid(raise_exception=True)

            user = UserService.create_user(req.validated_data)
            return api_response(True, Messages.PRODUCT_CREATED, user, StatusCodes.HTTP_201_CREATED)
        
        except Exception as e:
            return api_response(False, str(e), None, StatusCodes.HTTP_500_INTERNAL_SERVER_ERROR)
    
