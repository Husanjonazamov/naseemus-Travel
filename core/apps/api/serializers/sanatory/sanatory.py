from rest_framework import serializers

from core.apps.api.models import SanatoryModel


class BaseSanatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SanatoryModel
        fields = [
            "id",
            "name",
        ]


class ListSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta): ...


class RetrieveSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta): ...


class CreateSanatorySerializer(BaseSanatorySerializer):
    class Meta(BaseSanatorySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
