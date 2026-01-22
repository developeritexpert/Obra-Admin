from django.contrib.auth import get_user_model

User = get_user_model()

class UserRepository:

    @staticmethod
    def get_by_email(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(email, password, role):
        return User.objects.create_user(
            email=email,
            password=password,
            role=role
        )

    @staticmethod
    def admin_exists():
        return User.objects.filter(role="admin").exists()