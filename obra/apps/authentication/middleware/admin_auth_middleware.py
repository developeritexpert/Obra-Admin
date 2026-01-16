from django.shortcuts import redirect


class AdminJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/dashboard"):
            if not request.session.get("access_token"):
                return redirect("/auth/admin/login")
        return self.get_response(request)
