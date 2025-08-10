from django import forms

from core.apps.api.models import FeatureModel


class FeatureForm(forms.ModelForm):

    class Meta:
        model = FeatureModel
        fields = "__all__"
