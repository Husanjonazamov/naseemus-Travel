from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import PostingTypeModel


@admin.register(PostingTypeModel)
class PostingAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
