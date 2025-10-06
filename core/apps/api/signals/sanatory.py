from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import SanatoryModel, VideoModel


@receiver(post_save, sender=SanatoryModel)
def SanatorySignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=VideoModel)
def VideoSignal(sender, instance, created, **kwargs): ...
