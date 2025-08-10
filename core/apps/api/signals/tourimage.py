from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import TourimageModel


@receiver(post_save, sender=TourimageModel)
def TourimageSignal(sender, instance, created, **kwargs): ...
