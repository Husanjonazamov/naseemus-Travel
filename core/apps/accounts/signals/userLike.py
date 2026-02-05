from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import UserLikeModel


@receiver(post_save, sender=UserLikeModel)
def UserLikeSignal(sender, instance, created, **kwargs): ...

