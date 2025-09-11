from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import HolidayitemModel
from core.apps.api.serializers.holidayItem import (
    CreateHolidayitemSerializer,
    ListHolidayitemSerializer,
    RetrieveHolidayitemSerializer,
)


@extend_schema(tags=["HolidayItem"])
class HolidayitemView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = HolidayitemModel.objects.all()
    serializer_class = ListHolidayitemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHolidayitemSerializer,
        "retrieve": RetrieveHolidayitemSerializer,
        "create": CreateHolidayitemSerializer,
    }
