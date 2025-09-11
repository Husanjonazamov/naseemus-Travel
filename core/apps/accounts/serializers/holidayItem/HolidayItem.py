from rest_framework import serializers

from core.apps.accounts.models import HolidayitemModel


class BaseHolidayitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayitemModel
        fields = [
            "id",
            "name",
        ]


class ListHolidayitemSerializer(BaseHolidayitemSerializer):
    class Meta(BaseHolidayitemSerializer.Meta): ...


class RetrieveHolidayitemSerializer(BaseHolidayitemSerializer):
    class Meta(BaseHolidayitemSerializer.Meta): ...


class CreateHolidayitemSerializer(BaseHolidayitemSerializer):
    class Meta(BaseHolidayitemSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
