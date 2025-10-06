from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import HotelModel
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(HotelModel)
class HotelAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
    )
