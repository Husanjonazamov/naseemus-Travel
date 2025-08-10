from django import forms

from core.apps.api.models import BlogModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = "__all__"
