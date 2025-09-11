from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import HolidaysimageModel, HolidaysModel


@receiver(post_save, sender=HolidaysModel)
def HolidaysSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=HolidaysimageModel)
def HolidaysimageSignal(sender, instance, created, **kwargs): ...
