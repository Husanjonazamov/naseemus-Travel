from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import FeatureModel
from core.apps.api.serializers.feature import CreateFeatureSerializer, ListFeatureSerializer, RetrieveFeatureSerializer


@extend_schema(tags=["feature"])
class FeatureView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = FeatureModel.objects.all()
    serializer_class = ListFeatureSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFeatureSerializer,
        "retrieve": RetrieveFeatureSerializer,
        "create": CreateFeatureSerializer,
    }
