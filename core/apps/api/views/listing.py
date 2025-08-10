from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ListingimageModel, ListingModel
from core.apps.api.serializers.listing import (
    CreateListingimageSerializer,
    CreateListingSerializer,
    ListListingimageSerializer,
    ListListingSerializer,
    RetrieveListingimageSerializer,
    RetrieveListingSerializer,
)


@extend_schema(tags=["listing"])
class ListingView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingModel.objects.all()
    serializer_class = ListListingSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListListingSerializer,
        "retrieve": RetrieveListingSerializer,
        "create": CreateListingSerializer,
    }


@extend_schema(tags=["listingImage"])
class ListingimageView(BaseViewSetMixin, ModelViewSet):
    queryset = ListingimageModel.objects.all()
    serializer_class = ListListingimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListListingimageSerializer,
        "retrieve": RetrieveListingimageSerializer,
        "create": CreateListingimageSerializer,
    }
