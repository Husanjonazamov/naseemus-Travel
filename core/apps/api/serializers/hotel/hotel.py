from rest_framework import serializers

from core.apps.api.models import HotelModel


class BaseHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = [
            "id",
            "title",
            "image",
            "description"
        ]


class ListHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta): ...


class RetrieveHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta): ...


class CreateHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta):
        fields = [
            "id",
            "title",
            "image",
            "description"
        ]
