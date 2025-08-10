from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.payment.models import PaymeModel


@receiver(post_save, sender=PaymeModel)
def PaymeSignal(sender, instance, created, **kwargs): ...
