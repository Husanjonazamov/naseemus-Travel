from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import HolidayitemModel


@admin.register(HolidayitemModel)
class HolidayitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
