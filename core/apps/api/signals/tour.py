from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import TourModel


@receiver(post_save, sender=TourModel)
def TourSignal(sender, instance, created, **kwargs): ...
