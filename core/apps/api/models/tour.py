from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TourModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    price = models.DecimalField(verbose_name=_("Narxi"), max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name=_("Image"), upload_to="tour/")
    date = models.IntegerField(verbose_name=_("Kun"), blank=True, null=True)
    is_popular = models.BooleanField(verbose_name=_("Mashhurmi ?"), default=False)
    is_new = models.BooleanField(verbose_name=_("Yangi ?"), default=True)
        
    
    
    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "tour"
        verbose_name = _("TourModel")
        verbose_name_plural = _("TourModels")
