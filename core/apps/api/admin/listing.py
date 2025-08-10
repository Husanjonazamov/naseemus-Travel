from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ListingimageModel, ListingModel


@admin.register(ListingModel)
class ListingAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ListingimageModel)
class ListingimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
