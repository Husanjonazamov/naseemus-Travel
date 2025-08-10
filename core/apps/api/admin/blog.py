from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BlogModel


@admin.register(BlogModel)
class BlogAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
