from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import HotelModel


@register(HotelModel)
class HotelTranslation(TranslationOptions):
    fields = [
        "title",
        "description"
    ]
