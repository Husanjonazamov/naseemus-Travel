from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.payment.models import PaymeModel


@admin.register(PaymeModel)
class PaymeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
