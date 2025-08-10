from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import TourModel


@register(TourModel)
class TourTranslation(TranslationOptions):
    fields = []
