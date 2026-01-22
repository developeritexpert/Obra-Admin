from django.urls import path
from apps.users.controllers.user_controller import UserCreateController

urlpatterns = [
    path('create/', UserCreateController.as_view()),
    path('get-users/', UserCreateController.as_view()),
]
