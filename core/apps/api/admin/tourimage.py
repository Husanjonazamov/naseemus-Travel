from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import TourimageModel


@admin.register(TourimageModel)
class TourimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
