from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BlogModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    image = models.ImageField(verbose_name=_("Rasm"), upload_to="blog/")

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "blog"
        verbose_name = _("BlogModel")
        verbose_name_plural = _("BlogModels")
