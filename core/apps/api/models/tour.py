from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django_core.models import AbstractBaseModel


class TourModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    category = models.ForeignKey("api.CategoryModel", on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(verbose_name=_("Narxi"), max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name=_("Image"), upload_to="tour/")
    maps = models.ImageField(upload_to="maps/", verbose_name=_("Xarita"), blank=True, null=True)
    date = models.IntegerField(verbose_name=_("Kun"), blank=True, null=True)
    is_popular = models.BooleanField(verbose_name=_("Mashhurmi ?"), default=False)
    is_new = models.BooleanField(verbose_name=_("Yangi ?"), default=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug: 
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while TourModel.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            title="mock",
            price=100,
            image="tour/mock.jpg",
        )

    class Meta:
        db_table = "tour"
        verbose_name = _("TourModel")
        verbose_name_plural = _("TourModels")
