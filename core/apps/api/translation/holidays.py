from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import HolidaysimageModel, HolidaysModel


@register(HolidaysModel)
class HolidaysTranslation(TranslationOptions):
    fields = []


@register(HolidaysimageModel)
class HolidaysimageTranslation(TranslationOptions):
    fields = []
