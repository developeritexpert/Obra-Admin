# apps/auth/urls.py
from django.urls import path
from apps.authentication.controllers.admin.admin_auth_controller import admin_login , admin_logout
# from obra.apps.authentication.controllers.api.login_controller import api_login
# from apps.authentication.controllers.api.logout_controller import api_logout

app_name = "auth"

urlpatterns = [
    # Admin (template-based)
    path("admin/login", admin_login, name="admin-login"),
    path("admin/logout", admin_logout, name="admin-logout"),

]
