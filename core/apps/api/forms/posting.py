from django import forms

from core.apps.api.models import PostingTypeModel


class PostingForm(forms.ModelForm):

    class Meta:
        model = PostingTypeModel
        fields = "__all__"
