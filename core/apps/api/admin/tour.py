from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import TourModel, TourimageModel


class TourImageInlines(TabularInline):
    model = TourimageModel
    extra = 2
    

@admin.register(TourModel)
class TourAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "image_tag",
        "title",
        "description_short",
        "price_display",
        "date",
        "is_popular",
        "is_new"
    )
    prepopulated_fields = {"slug": ("title",)}

    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_filter = ("is_popular", "is_new", "date")

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="40" style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = "Image"

    def description_short(self, obj):
        return (obj.description[:50] + "...") if obj.description else "-"
    description_short.short_description = "Description"

    def price_display(self, obj):
        return f"${obj.price:,.2f}"
    price_display.short_description = "Price"
    
    inlines = [TourImageInlines]
