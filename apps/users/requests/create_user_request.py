from rest_framework import serializers

class CreateUserRequest(serializers.Serializer):
    email = serializers.EmailField()
    role = serializers.CharField()
    password = serializers.CharField(min_length=8)
