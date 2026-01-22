from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserRepository:
    @staticmethod
    def get_admin_by_email(email: str):
        try:
            return User.objects.get(
                email=email,
                is_active=True,
                role=User.Role.ADMIN,
            )
        except User.DoesNotExist:
            return None

    @staticmethod
    def verify_password(user: User, raw_password: str) -> bool:
        return check_password(raw_password, user.password)
