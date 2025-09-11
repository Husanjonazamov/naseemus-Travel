from django import forms

from core.apps.api.models import BannerModel


class BanerForm(forms.ModelForm):

    class Meta:
        model = BannerModel
        fields = "__all__"
