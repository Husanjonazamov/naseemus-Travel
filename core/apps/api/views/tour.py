from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import TourModel
from core.apps.api.serializers.tour import CreateTourSerializer, ListTourSerializer, RetrieveTourSerializer


@extend_schema(tags=["tour"])
class TourView(BaseViewSetMixin, ModelViewSet):
    queryset = TourModel.objects.all()
    serializer_class = ListTourSerializer
    permission_classes = [AllowAny]
    
    lookup_field = 'title'
    lookup_url_kwarg = 'title'  # url parametri nomi

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTourSerializer,
        "retrieve": RetrieveTourSerializer,
        "create": CreateTourSerializer,
    }
