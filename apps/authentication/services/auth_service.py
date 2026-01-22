from django.contrib.auth.hashers import check_password
from apps.authentication.repositories.user_repository import UserRepository
from apps.authentication.services.jwt_service import JWTService


class AuthService:

    @staticmethod
    def login(email, password):
        user = UserRepository.get_by_email(email)

        if not user:
            return None, "Invalid credentials"

        if not check_password(password, user.password):
            return None, "Invalid credentials"

        token = JWTService.generate_token(user)

        return {
            "user": user,
            "token": token,
        }, None

    @staticmethod
    def register(email, password, role):
        if UserRepository.get_by_email(email):
            return None, "Email already registered"

        user = UserRepository.create_user(email, password, role)
        return user, None


    @staticmethod
    def admin_exists():
        return UserRepository.admin_exists()