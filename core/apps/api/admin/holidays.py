from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from core.apps.api.models import HolidaysimageModel, HolidaysModel


class HolidaysimageInline(TabularInline):
    model = HolidaysimageModel
    extra = 1  


@admin.register(HolidaysModel)
class HolidaysAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [HolidaysimageInline]


@admin.register(HolidaysimageModel)
class HolidaysimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
