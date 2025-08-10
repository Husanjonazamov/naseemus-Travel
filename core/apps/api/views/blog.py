from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import BlogModel
from core.apps.api.serializers.blog import CreateBlogSerializer, ListBlogSerializer, RetrieveBlogSerializer


@extend_schema(tags=["blog"])
class BlogView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = ListBlogSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBlogSerializer,
        "retrieve": RetrieveBlogSerializer,
        "create": CreateBlogSerializer,
    }
