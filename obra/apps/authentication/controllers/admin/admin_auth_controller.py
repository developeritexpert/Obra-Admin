from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied
from apps.authentication.services.auth_service import AdminAuthService


@csrf_protect
def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me") == "on"

        try:
            tokens = AdminAuthService.login(
                request=request,
                email=email,
                password=password,
                remember_me=remember_me,
            )

            # Store JWT in session (HTTP-only via Django session)
            request.session["access_token"] = tokens["access"]
            request.session["refresh_token"] = tokens["refresh"]

            return redirect("/admin/dashboard/")

        except PermissionDenied as e:
            return render(
                request,
                "auth/admin_login.html",
                {"error": str(e)},
            )

    return render(request, "auth/admin_login.html")


def admin_logout(request):
    AdminAuthService.logout(request)
    return redirect("/auth/admin/login")