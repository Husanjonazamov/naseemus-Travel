from django import forms

from core.apps.accounts.models import HolidayitemModel


class HolidayitemForm(forms.ModelForm):

    class Meta:
        model = HolidayitemModel
        fields = "__all__"
