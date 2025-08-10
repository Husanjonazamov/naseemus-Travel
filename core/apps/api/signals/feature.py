from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import FeatureModel


@receiver(post_save, sender=FeatureModel)
def FeatureSignal(sender, instance, created, **kwargs): ...
