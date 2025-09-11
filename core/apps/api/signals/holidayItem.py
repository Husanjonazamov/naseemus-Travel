from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import HolidayitemModel


@receiver(post_save, sender=HolidayitemModel)
def HolidayitemSignal(sender, instance, created, **kwargs): ...
