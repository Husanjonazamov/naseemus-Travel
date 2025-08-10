from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import PostingTypeModel


@receiver(post_save, sender=PostingTypeModel)
def PostingSignal(sender, instance, created, **kwargs): ...
