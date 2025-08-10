from modeltranslation.translator import TranslationOptions, register

from core.apps.payment.models import PaymeModel


@register(PaymeModel)
class PaymeTranslation(TranslationOptions):
    fields = []
