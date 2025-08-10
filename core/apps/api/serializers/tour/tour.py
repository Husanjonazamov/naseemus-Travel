from rest_framework import serializers

from core.apps.api.models import TourModel


class BaseTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourModel
        fields = [
            "id",
            "name",
        ]


class ListTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class RetrieveTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class CreateTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
