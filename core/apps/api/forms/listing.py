from django import forms

from core.apps.api.models import ListingimageModel, ListingModel


class ListingForm(forms.ModelForm):

    class Meta:
        model = ListingModel
        fields = "__all__"


class ListingimageForm(forms.ModelForm):

    class Meta:
        model = ListingimageModel
        fields = "__all__"
