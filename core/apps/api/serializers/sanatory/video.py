from rest_framework import serializers

from core.apps.api.models import VideoModel


class BaseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = [
            "id",
            "name",
        ]


class ListVideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta): ...


class RetrieveVideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta): ...


class CreateVideoSerializer(BaseVideoSerializer):
    class Meta(BaseVideoSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
