from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from obra.apps.authentication.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        USER = "user", "User"   
        TRADER = "trader", "Trader"

    # Core Identity Fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)    
    
    # Authentication
    password = models.CharField(max_length=128)

    # Authorization
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER
    )

    # Account Status
    is_active = models.BooleanField(default=True)

    # Email Verification
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)

    # Password Reset
    reset_password_token = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )
    reset_password_expires = models.DateTimeField(
        null=True,
        blank=True
    )

    # Profile
    image_url = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # Authentication Config
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["role"]),
            models.Index(fields=["reset_password_token"]),
        ]