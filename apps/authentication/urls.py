from django.urls import path
from apps.authentication.controllers.common.auth_controller import (
    login_view,
    logout_view,
    register_user_view,
    register_trader_view,
    register_admin_view,
)

app_name = "auth"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Registration
    path("register/user/", register_user_view, name="register_user"),
    path("register/trader/", register_trader_view, name="register_trader"),

    path("register/admin/", register_admin_view, name="register_admin"),
]
