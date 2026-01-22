import jwt
from datetime import datetime, timedelta
from django.conf import settings


class JWTService:

    @staticmethod
    def generate_token(user):
        payload = {
            "user_id": user.id,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(hours=12),
            "iat": datetime.utcnow(),
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
