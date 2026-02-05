from django import forms

from core.apps.accounts.models import UserlikeModel


class UserlikeForm(forms.ModelForm):

    class Meta:
        model = UserlikeModel
        fields = "__all__"
