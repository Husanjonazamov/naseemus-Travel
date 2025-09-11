from django_filters import rest_framework as filters

from core.apps.api.models import HolidaysimageModel, HolidaysModel


class HolidaysFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = HolidaysModel
        fields = [
            "name",
        ]


class HolidaysimageFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = HolidaysimageModel
        fields = [
            "name",
        ]
