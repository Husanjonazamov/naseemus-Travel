from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import SanatoryModel, VideoModel
from core.apps.api.serializers.sanatory import (
    CreateSanatorySerializer,
    CreateVideoSerializer,
    ListSanatorySerializer,
    ListVideoSerializer,
    RetrieveSanatorySerializer,
    RetrieveVideoSerializer,
)


@extend_schema(tags=["sanatory"])
class SanatoryView(BaseViewSetMixin, ModelViewSet):
    queryset = SanatoryModel.objects.all()
    serializer_class = ListSanatorySerializer
    permission_classes = [AllowAny]
    
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug' 

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSanatorySerializer,
        "retrieve": RetrieveSanatorySerializer,
        "create": CreateSanatorySerializer,
    }


@extend_schema(tags=["video"])
class VideoView(BaseViewSetMixin, ModelViewSet):
    queryset = VideoModel.objects.all()
    serializer_class = ListVideoSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListVideoSerializer,
        "retrieve": RetrieveVideoSerializer,
        "create": CreateVideoSerializer,
    }
