from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserLikeModel(AbstractBaseModel):

    user = models.ForeignKey(
        "accounts.User", 
        on_delete=models.CASCADE, 
        related_name="likes",
        verbose_name=_("Foydalanuvchi")
    )
    tour = models.ForeignKey(
        "api.TourModel", 
        on_delete=models.CASCADE, 
        related_name="user_likes",
        verbose_name=_("Tur")
    )

    def __str__(self):
        return f"{self.user.email} -> {self.tour.title}"

    class Meta:
        db_table = "UserLike"
        verbose_name = _("UserLikeModel")
        verbose_name_plural = _("UserLikeModels")
        unique_together = ("user", "tour")
