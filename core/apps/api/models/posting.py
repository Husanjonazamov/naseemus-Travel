from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PostingTypeModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Turi"), max_length=255)
    price = models.DecimalField(
        verbose_name=_("Narxi"),
        max_digits=20,
        decimal_places=2 
    )
    feature = models.ManyToManyField(
        "api.FeatureModel",
        verbose_name=_("Xususiyatlar"),
        blank=True 
    )
    
    

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "posting"
        verbose_name = _("PostingTypeModel")
        verbose_name_plural = _("PostingTypeModels")
