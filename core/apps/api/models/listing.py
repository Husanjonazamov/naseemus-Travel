from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ListingModel(AbstractBaseModel):
    address = models.TextField(verbose_name=_("Manzil"))
    full_name = models.CharField(verbose_name=_("To'liq ism"), max_length=200)
    contact_time = models.CharField(verbose_name=_("Murojat vaqti"), max_length=50)
    category = models.ForeignKey("api.CategoryModel", on_delete=models.CASCADE)
    posting_type = models.ForeignKey("api.PostingTypeModel", verbose_name=_("Elon turi"), on_delete=models.CASCADE, related_name="posting")
    specialty = models.CharField(verbose_name=_("Mutaxasislik"), max_length=300)
    price = models.DecimalField(verbose_name=_("Narxi"), max_digits=10, decimal_places=2)
    age = models.IntegerField(verbose_name=_("Yosh"))
    bio = models.TextField(verbose_name=_("Bio"))
    image = models.ImageField(verbose_name=_("Rasm"), upload_to="listing/")
    phone = models.CharField(verbose_name=_("Telefon raqam"), max_length=100)
    telegram = models.CharField(verbose_name=_("Telegram"), max_length=200)
    
    

    def __str__(self):
        return str(self.full_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "listing"
        verbose_name = _("ListingModel")
        verbose_name_plural = _("ListingModels")


class ListingimageModel(AbstractBaseModel):
    listing = models.ForeignKey(ListingModel, on_delete=models.CASCADE, related_name="images")
    
    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "listingImage"
        verbose_name = _("ListingimageModel")
        verbose_name_plural = _("ListingimageModels")
