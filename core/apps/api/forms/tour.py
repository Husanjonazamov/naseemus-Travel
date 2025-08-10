from django import forms

from core.apps.api.models import TourModel


class TourForm(forms.ModelForm):

    class Meta:
        model = TourModel
        fields = "__all__"
