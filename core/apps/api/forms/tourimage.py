from django import forms

from core.apps.api.models import TourimageModel


class TourimageForm(forms.ModelForm):

    class Meta:
        model = TourimageModel
        fields = "__all__"
