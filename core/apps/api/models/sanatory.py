from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify
from django.utils.text import slugify


class SanatoryModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255, unique=True, blank=True)
    price = models.DecimalField(verbose_name=_("Narxi"), max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name=_("Tavsif"))
    image = models.ImageField(verbose_name=_("Rasm"), upload_to="sanatory-images/")

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )
        
    def save(self, *args, **kwargs):
        if not self.slug: 
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while SanatoryModel.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

        
        
    class Meta:
        db_table = "sanatory"
        verbose_name = _("SanatoryModel")
        verbose_name_plural = _("SanatoryModels")




class VideoModel(AbstractBaseModel):
    sanatory = models.ForeignKey(SanatoryModel, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(verbose_name=_("Video"), upload_to="video/")

    def __str__(self):
        return str(self.sanatory.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "video"
        verbose_name = _("VideoModel")
        verbose_name_plural = _("VideoModels")
