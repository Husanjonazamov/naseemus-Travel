from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TourimageModel(AbstractBaseModel):
    tour = models.ForeignKey("api.TourModel", on_delete=models.CASCADE, blank=True, null=True, related_name="images")
    image = models.ImageField(upload_to="image/", blank=True, null=True)

    def __str__(self):
        return str(self.tour.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "tourimage"
        verbose_name = _("TourimageModel")
        verbose_name_plural = _("TourimageModels")
