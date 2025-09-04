from rest_framework import serializers

from core.apps.api.models import TourModel


class BaseTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourModel
        fields = [
            "id",
            "title",
            "description",
            "price",
            "image",
            "date",
            "is_popular",
            "is_new"
        ]


class ListTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class RetrieveTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class CreateTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
