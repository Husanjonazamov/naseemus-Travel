from rest_framework import serializers

from core.apps.api.models import HolidaysModel
from core.apps.api.serializers.holidays.holidaysImage import BaseHolidaysimageSerializer


class BaseHolidaysSerializer(serializers.ModelSerializer):
    images = BaseHolidaysimageSerializer(many=True, read_only=True, source="holdays")

    class Meta:
        model = HolidaysModel
        fields = [
            "id",
            "title", 
            "description", 
            "image", 
            "images"
        ]

class ListHolidaysSerializer(BaseHolidaysSerializer):
    class Meta(BaseHolidaysSerializer.Meta): ...


class RetrieveHolidaysSerializer(BaseHolidaysSerializer):
    class Meta(BaseHolidaysSerializer.Meta): ...


class CreateHolidaysSerializer(BaseHolidaysSerializer):
    class Meta(BaseHolidaysSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
