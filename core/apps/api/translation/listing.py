from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ListingimageModel, ListingModel


@register(ListingModel)
class ListingTranslation(TranslationOptions):
    fields = []


@register(ListingimageModel)
class ListingimageTranslation(TranslationOptions):
    fields = []
