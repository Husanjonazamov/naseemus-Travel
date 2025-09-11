from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import BannerModel
from core.apps.api.serializers.banner import CreateBanerSerializer, ListBanerSerializer, RetrieveBanerSerializer


@extend_schema(tags=["baner"])
class BanerView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = ListBanerSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBanerSerializer,
        "retrieve": RetrieveBanerSerializer,
        "create": CreateBanerSerializer,
    }
