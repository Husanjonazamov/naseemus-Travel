from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import BlogModel


@receiver(post_save, sender=BlogModel)
def BlogSignal(sender, instance, created, **kwargs): ...
