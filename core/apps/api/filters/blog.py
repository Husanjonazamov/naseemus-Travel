from django_filters import rest_framework as filters

from core.apps.api.models import BlogModel


class BlogFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = BlogModel
        fields = [
            "name",
        ]
