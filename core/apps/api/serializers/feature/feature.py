from rest_framework import serializers

from core.apps.api.models import FeatureModel


class BaseFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureModel
        fields = [
            "id",
            "title",
        ]


class ListFeatureSerializer(BaseFeatureSerializer):
    class Meta(BaseFeatureSerializer.Meta): ...


class RetrieveFeatureSerializer(BaseFeatureSerializer):
    class Meta(BaseFeatureSerializer.Meta): ...


class CreateFeatureSerializer(BaseFeatureSerializer):
    class Meta(BaseFeatureSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
