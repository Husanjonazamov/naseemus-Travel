from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import UserLikeModel


@admin.register(UserLikeModel)
class UserLikeAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "tour",
        "created_at",
    )

