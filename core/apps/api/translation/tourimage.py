from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import TourimageModel


@register(TourimageModel)
class TourimageTranslation(TranslationOptions):
    fields = []
