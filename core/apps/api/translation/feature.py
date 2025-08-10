from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import FeatureModel


@register(FeatureModel)
class FeatureTranslation(TranslationOptions):
    fields = []
