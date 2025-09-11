from rest_framework import serializers

from core.apps.api.models import HolidaysimageModel


class BaseHolidaysimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaysimageModel
        fields = [
            "id",
            "image",
        ]


class ListHolidaysimageSerializer(BaseHolidaysimageSerializer):
    class Meta(BaseHolidaysimageSerializer.Meta): ...


class RetrieveHolidaysimageSerializer(BaseHolidaysimageSerializer):
    class Meta(BaseHolidaysimageSerializer.Meta): ...


class CreateHolidaysimageSerializer(BaseHolidaysimageSerializer):
    class Meta(BaseHolidaysimageSerializer.Meta):
        fields = [
            "id",
            "image",
        ]
