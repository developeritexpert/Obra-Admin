from rest_framework.response import Response
from apps.core.constants.status_codes import StatusCodes

def api_response(status, message, data = None, status_code = StatusCodes.HTTP_200_OK):
    response = {
        "success": status,
        "status_code": status_code,
        "message": message,
        "data": data
    }
    return Response(response, status=status_code)
