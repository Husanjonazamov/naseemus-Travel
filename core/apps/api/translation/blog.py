from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BlogModel


@register(BlogModel)
class BlogTranslation(TranslationOptions):
    fields = []
