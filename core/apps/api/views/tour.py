from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import TourModel
from core.apps.api.serializers.tour import CreateTourSerializer, ListTourSerializer, RetrieveTourSerializer

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


@extend_schema(tags=["tour"])
class TourView(BaseViewSetMixin, ModelViewSet):
    queryset = TourModel.objects.all()
    serializer_class = ListTourSerializer
    permission_classes = [AllowAny]
    
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'  # url parametri nomi

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTourSerializer,
        "retrieve": RetrieveTourSerializer,
        "create": CreateTourSerializer,
    }


    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request, *args, **kwargs):
        search_value = request.query_params.get("search")
        qs = self.queryset

        if search_value:
            if search_value.isdigit():  # agar son bo‘lsa -> price bo‘yicha
                qs = qs.filter(price=search_value)
            else:  # faqat title bo‘yicha qidiradi
                qs = qs.filter(title__icontains=search_value)

        serializer = ListTourSerializer(qs, many=True)
        return Response(serializer.data)