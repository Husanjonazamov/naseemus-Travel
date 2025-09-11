from rest_framework import serializers

from core.apps.api.models import BannerModel


class BaseBanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = [
            "id",
            "title",
            "image"
        ]


class ListBanerSerializer(BaseBanerSerializer):
    class Meta(BaseBanerSerializer.Meta): ...


class RetrieveBanerSerializer(BaseBanerSerializer):
    class Meta(BaseBanerSerializer.Meta): ...


class CreateBanerSerializer(BaseBanerSerializer):
    class Meta(BaseBanerSerializer.Meta):
        fields = [
            "id",
            "title",
            "image"
        ]
