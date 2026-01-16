from apps.users.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(validated_data):
        password = validated_data.pop('password')
        user = UserRepository.create_user(validated_data)
        user.set_password(password)
        user.save()
        return user
