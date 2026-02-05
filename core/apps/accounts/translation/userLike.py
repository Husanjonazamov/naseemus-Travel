from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import UserLikeModel


@register(UserLikeModel)
class UserLikeTranslation(TranslationOptions):
    fields = []

