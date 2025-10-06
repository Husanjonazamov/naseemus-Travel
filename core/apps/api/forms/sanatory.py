from django import forms

from core.apps.api.models import SanatoryModel, VideoModel


class SanatoryForm(forms.ModelForm):

    class Meta:
        model = SanatoryModel
        fields = "__all__"


class VideoForm(forms.ModelForm):

    class Meta:
        model = VideoModel
        fields = "__all__"
