from rest_framework import serializers

from core.apps.api.models import TourimageModel


class BaseTourimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourimageModel
        fields = [
            "id",
            "name",
        ]


class ListTourimageSerializer(BaseTourimageSerializer):
    class Meta(BaseTourimageSerializer.Meta): ...


class RetrieveTourimageSerializer(BaseTourimageSerializer):
    class Meta(BaseTourimageSerializer.Meta): ...


class CreateTourimageSerializer(BaseTourimageSerializer):
    class Meta(BaseTourimageSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
