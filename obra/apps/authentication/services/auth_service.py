from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.repositories.user_repository import UserRepository


class AdminAuthService:

    @staticmethod
    def login(request, email: str, password: str, remember_me: bool = False):
        user = UserRepository.get_admin_by_email(email)

        if not user:
            raise PermissionDenied("Invalid email or password")

        if not UserRepository.verify_password(user, password):
            raise PermissionDenied("Invalid email or password")

        # if not user.is_staff:
        #     raise PermissionDenied("Admin access required")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Remember-me logic (session lifetime)
        if remember_me:
            request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
        else:
            request.session.set_expiry(0)  # browser session

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "email": user.email,
        }

    @staticmethod
    def logout(request):
        request.session.flush()
