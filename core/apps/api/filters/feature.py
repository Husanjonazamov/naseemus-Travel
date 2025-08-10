from django_filters import rest_framework as filters

from core.apps.api.models import FeatureModel


class FeatureFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = FeatureModel
        fields = [
            "name",
        ]
