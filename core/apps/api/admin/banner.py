from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BannerModel


@admin.register(BannerModel)
class BanerAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
