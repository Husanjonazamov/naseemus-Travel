from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from core.apps.api.models import BlogModel


@admin.register(BlogModel)
class BlogAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
        "display_image",  # custom method nomi
        "description"
    )

    def display_image(self, obj):
        if obj.image:  # agar rasm bo‘lsa
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;"/>', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"
