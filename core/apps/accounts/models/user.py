from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..choices import RoleChoice
from ..managers import UserManager


class User(auth_models.AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.USER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"] # Admin or create_user requires these
    objects = UserManager()

    def __str__(self):
        return self.email

