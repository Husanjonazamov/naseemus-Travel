from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import HolidayitemModel


@register(HolidayitemModel)
class HolidayitemTranslation(TranslationOptions):
    fields = []
