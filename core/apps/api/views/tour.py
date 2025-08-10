from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import TourModel
from core.apps.api.serializers.tour import CreateTourSerializer, ListTourSerializer, RetrieveTourSerializer


@extend_schema(tags=["tour"])
class TourView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TourModel.objects.all()
    serializer_class = ListTourSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTourSerializer,
        "retrieve": RetrieveTourSerializer,
        "create": CreateTourSerializer,
    }
