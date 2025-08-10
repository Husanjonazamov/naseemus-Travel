from django import forms

from core.apps.payment.models import PaymeModel


class PaymeForm(forms.ModelForm):

    class Meta:
        model = PaymeModel
        fields = "__all__"
