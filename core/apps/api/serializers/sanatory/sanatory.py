from rest_framework import serializers

from core.apps.api.models import SanatoryModel
from core.apps.api.serializers.sanatory.video import ListVideoSerializer


class BaseSanatorySerializer(serializers.ModelSerializer):
    videos = ListVideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = SanatoryModel
        fields = [
            "id",
            "title",
            "slug",
            "date",
            "price",
            "description",
            "image",
            "videos",
        ]


class ListSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta): ...


class RetrieveSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta): ...


class CreateSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta):
        fields = [
            "id",
            "title",
            "price",
            "description",
            "image",
            "videos",
        ]