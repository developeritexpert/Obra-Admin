from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from obra.apps.authentication.services.auth_service import AuthService


ROLE_DASHBOARD = {
    "admin": "/admin/dashboard/",
    "user": "/user/dashboard/",
    "trader": "/trader/dashboard/",
}


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        result, error = AuthService.login(email, password)

        if error:
            return render(request, "auth/login.html", {"error": error})

        user = result["user"]
        token = result["token"]

        response = redirect(ROLE_DASHBOARD.get(user.role, "/user/dashboard/"))
        response.set_cookie(
            "access_token",
            token,
            httponly=True,
            samesite="Lax",
            secure=False,  # True in production
        )
        return response

    # Check if user , trader or admin is already logged in check cookie token and get user type info and redirect to dashboard
    

    return render(request, "auth/login.html")


@require_POST
def logout_view(request):
    response = redirect("/auth/login/")
    response.delete_cookie(
        "access_token",
        path="/",
    )
    return response



def register_user_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validate password confirmation
        if password != confirm_password:
            return render(
                request, 
                "auth/register_user.html", 
                {"error": "Passwords do not match"}
            )

        _, error = AuthService.register(email, password, role="user")

        if error:
            return render(request, "auth/register_user.html", {"error": error})

        return redirect("/auth/login/")

    return render(request, "auth/register_user.html")


def register_trader_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validate password confirmation
        if password != confirm_password:
            return render(
                request, 
                "auth/register_trader.html", 
                {"error": "Passwords do not match"}
            )

        _, error = AuthService.register(email, password, role="trader")

        if error:
            return render(request, "auth/register_trader.html", {"error": error})

        return redirect("/auth/login/")

    return render(request, "auth/register_trader.html")

def register_admin_view(request):

    if AuthService.admin_exists():
        return redirect("/auth/login/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(
                request,
                "auth/register_admin.html",
                {"error": "Passwords do not match"},
            )

        _, error = AuthService.register(email, password, role="admin")

        if error:
            return render(
                request,
                "auth/register_admin.html",
                {"error": error},
            )

        return redirect("/auth/login/")

    return render(request, "auth/register_admin.html")