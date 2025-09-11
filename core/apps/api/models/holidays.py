from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class HolidaysModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    image = models.ImageField(upload_to="holidays", blank=True, null=True)
    # item = models.ManyToManyField("api.HolidayitemModel", verbose_name=_("Bayram ichidagi narsalar"))

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "holidays"
        verbose_name = _("HolidaysModel")
        verbose_name_plural = _("HolidaysModels")


class HolidaysimageModel(AbstractBaseModel):
    holidays = models.ForeignKey(HolidaysModel, on_delete=models.CASCADE, related_name="holdays")
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.holidays.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "holidaysImage"
        verbose_name = _("HolidaysimageModel")
        verbose_name_plural = _("HolidaysimageModels")
