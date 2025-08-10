from rest_framework import serializers

from core.apps.payment.models import PaymeModel


class BasePaymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeModel
        fields = [
            "id",
            "name",
        ]


class ListPaymeSerializer(BasePaymeSerializer):
    class Meta(BasePaymeSerializer.Meta): ...


class RetrievePaymeSerializer(BasePaymeSerializer):
    class Meta(BasePaymeSerializer.Meta): ...


class CreatePaymeSerializer(BasePaymeSerializer):
    class Meta(BasePaymeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
