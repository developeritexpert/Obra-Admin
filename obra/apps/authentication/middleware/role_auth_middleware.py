import jwt
from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class RoleAuthMiddleware(MiddlewareMixin):

    PUBLIC_PATHS = (
        "/auth/login/",
        "/auth/logout/",
        "/auth/register/",
        "/static/",
    )

    ROLE_PREFIX = {
        "admin": "/admin/",
        "user": "/user/",
        "trader": "/trader/",
    }

    def process_request(self, request):
        path = request.path.rstrip("/") + "/"

        token = request.COOKIES.get("access_token")

        # --------------------------------------------------
        # Case 1: Public routes
        # --------------------------------------------------
        if path.startswith(self.PUBLIC_PATHS):
            # If user is already logged in and tries to access login
            if token and path == "/auth/login/":
                payload = self._decode_token(token)
                if payload:
                    role = payload.get("role")
                    return redirect(f"/{role}/dashboard/")
            return None

        # --------------------------------------------------
        # Case 2: Protected routes → token required
        # --------------------------------------------------
        if not token:
            return redirect("/auth/login/") 

        payload = self._decode_token(token)
        if not payload:
            return redirect("/auth/login/")

        role = payload.get("role")

        if not role:
            return redirect("/auth/login/")

        # Root redirect
        if path == "/":
            return redirect(f"/{role}/dashboard/")

        # Role-based access control
        role_prefix = self.ROLE_PREFIX.get(role)
        if not role_prefix or not path.startswith(role_prefix):
            return redirect(f"/{role}/dashboard/")

        # Attach user context
        request.user_id = payload.get("user_id")
        request.user_role = role

        return None

    def _decode_token(self, token):
        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
