from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BannerModel


@register(BannerModel)
class BanerTranslation(TranslationOptions):
    fields = []
