from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import TourModel


@admin.register(TourModel)
class TourAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
