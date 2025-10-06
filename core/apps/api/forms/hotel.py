from django import forms

from core.apps.api.models import HotelModel


class HotelForm(forms.ModelForm):

    class Meta:
        model = HotelModel
        fields = "__all__"
