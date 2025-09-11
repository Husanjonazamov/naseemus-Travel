from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import HolidaysimageModel, HolidaysModel
from core.apps.api.serializers.holidays import (
    CreateHolidaysimageSerializer,
    CreateHolidaysSerializer,
    ListHolidaysimageSerializer,
    ListHolidaysSerializer,
    RetrieveHolidaysimageSerializer,
    RetrieveHolidaysSerializer,
)


@extend_schema(tags=["holidays"])
class HolidaysView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = HolidaysModel.objects.all()
    serializer_class = ListHolidaysSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHolidaysSerializer,
        "retrieve": RetrieveHolidaysSerializer,
        "create": CreateHolidaysSerializer,
    }


@extend_schema(tags=["holidaysImage"])
class HolidaysimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = HolidaysimageModel.objects.all()
    serializer_class = ListHolidaysimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHolidaysimageSerializer,
        "retrieve": RetrieveHolidaysimageSerializer,
        "create": CreateHolidaysimageSerializer,
    }
