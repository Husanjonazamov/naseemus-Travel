from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class FeatureModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "feature"
        verbose_name = _("FeatureModel")
        verbose_name_plural = _("FeatureModels")
