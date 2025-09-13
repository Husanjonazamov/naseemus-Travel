from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class OrderModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Ism"), max_length=255)
    tour = models.ForeignKey("api.TourModel", on_delete=models.CASCADE, related_name="tour")
    phone = models.CharField(verbose_name=_("Telefon raqam"), max_length=100)
    quantity = models.IntegerField(verbose_name=_("Soni"), blank=True, null=True, default=1)
    data = models.DateField(verbose_name=_("kun"), blank=True, null=True)
    comment = models.TextField(verbose_name=_("Kamment"), blank=True, null=True)


    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
