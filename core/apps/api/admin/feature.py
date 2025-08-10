from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import FeatureModel


@admin.register(FeatureModel)
class FeatureAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
