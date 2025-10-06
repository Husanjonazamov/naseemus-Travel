from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import SanatoryModel, VideoModel


@register(SanatoryModel)
class SanatoryTranslation(TranslationOptions):
    fields = [
        "title",
        "description"
    ]


@register(VideoModel)
class VideoTranslation(TranslationOptions):
    fields = []
