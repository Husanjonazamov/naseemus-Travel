from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import PostingTypeModel
from core.apps.api.serializers.posting import (
    BasePostingTypeSerializer,
    ListPostingTypeSerializer,
    RetrievePostingTypeSerializer, 
    CreatePostingTypeSerializer
)

@extend_schema(tags=["posting"])
class PostingView(BaseViewSetMixin, ModelViewSet):
    queryset = PostingTypeModel.objects.all()
    serializer_class = ListPostingTypeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPostingTypeSerializer,
        "retrieve": RetrievePostingTypeSerializer,
        "create": CreatePostingTypeSerializer,
    }
