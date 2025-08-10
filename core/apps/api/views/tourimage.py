from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import TourimageModel
from core.apps.api.serializers.tourimage import (
    CreateTourimageSerializer,
    ListTourimageSerializer,
    RetrieveTourimageSerializer,
)


@extend_schema(tags=["tourimage"])
class TourimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TourimageModel.objects.all()
    serializer_class = ListTourimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTourimageSerializer,
        "retrieve": RetrieveTourimageSerializer,
        "create": CreateTourimageSerializer,
    }
