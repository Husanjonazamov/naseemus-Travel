from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from core.apps.accounts.models import UserLikeModel
from core.apps.api.models import TourModel
from core.apps.accounts.serializers.userLike import (
    CreateUserLikeSerializer,
    ListUserLikeSerializer,
)


@extend_schema(tags=["UserLike"])
class UserLikeView(BaseViewSetMixin, GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ListUserLikeSerializer

    def get_queryset(self):
        return UserLikeModel.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserLikeSerializer
        return ListUserLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tour_slug = serializer.validated_data.get("tour_slug")
        
        tour = TourModel.objects.get(slug=tour_slug)
        user = request.user
        
        like_qs = UserLikeModel.objects.filter(user=user, tour=tour)
        
        if like_qs.exists():
            like_qs.delete()
            return Response({"detail": "Like olib tashlandi", "liked": False}, status=status.HTTP_200_OK)
        else:
            UserLikeModel.objects.create(user=user, tour=tour)
            return Response({"detail": "Like bosildi", "liked": True}, status=status.HTTP_201_CREATED)


