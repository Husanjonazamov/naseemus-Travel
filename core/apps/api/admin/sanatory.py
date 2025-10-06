from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin
from django.utils.html import format_html

from core.apps.api.models import SanatoryModel, VideoModel




class VideoInline(TabularInline):  
    model = VideoModel
    extra = 1  
    fields = ("video", "video_preview")
    readonly_fields = ("video_preview",)

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="200" height="120" controls>'
                '<source src="{}" type="video/mp4">'
                "Sizning brauzeringiz videoni ko‘rsata olmaydi."
                "</video>",
                obj.video.url,
            )
        return "-"
    video_preview.short_description = "Video"


@admin.register(SanatoryModel)
class SanatoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "__str__", "image_preview")
    inlines = [VideoInline]
    prepopulated_fields = {"slug": ("title",)}  # title asosida slug avto hosil bo‘ladi

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Rasm"


@admin.register(VideoModel)
class VideoAdmin(ModelAdmin):
    list_display = ("id", "__str__", "video_preview")

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="120" height="80" controls>'
                '<source src="{}" type="video/mp4">'
                "Sizning brauzeringiz videoni ko‘rsata olmaydi."
                "</video>",
                obj.video.url,
            )
        return "-"
    video_preview.short_description = "Video"
