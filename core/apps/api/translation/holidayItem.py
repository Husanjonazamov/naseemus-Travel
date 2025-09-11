from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import HolidayitemModel


@register(HolidayitemModel)
class HolidayitemTranslation(TranslationOptions):
    fields = []
