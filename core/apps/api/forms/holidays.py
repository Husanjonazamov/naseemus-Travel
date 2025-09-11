from django import forms

from core.apps.api.models import HolidaysimageModel, HolidaysModel


class HolidaysForm(forms.ModelForm):

    class Meta:
        model = HolidaysModel
        fields = "__all__"


class HolidaysimageForm(forms.ModelForm):

    class Meta:
        model = HolidaysimageModel
        fields = "__all__"
