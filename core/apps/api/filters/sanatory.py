from django_filters import rest_framework as filters

from core.apps.api.models import SanatoryModel, VideoModel


class SanatoryFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = SanatoryModel
        fields = [
            "name",
        ]


class VideoFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = VideoModel
        fields = [
            "name",
        ]
