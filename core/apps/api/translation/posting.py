from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PostingTypeModel


@register(PostingTypeModel)
class PostingTranslation(TranslationOptions):
    fields = []
