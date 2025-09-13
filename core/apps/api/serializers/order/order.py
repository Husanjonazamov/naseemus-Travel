from rest_framework import serializers
from core.apps.api.models import OrderModel, TourModel
from .send import order_created_handler

class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ["id", "name"]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        fields = ["id", "name", "phone", "quantity", "data"]




class RetrieveOrderSerializer(serializers.ModelSerializer):
    tour = serializers.StringRelatedField(read_only=True) 
    tour_id = serializers.PrimaryKeyRelatedField(
        queryset=TourModel.objects.all(),
        source="tour",
        write_only=True,
    )

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "name",
            "phone",
            "quantity",
            "data",
            "comment",
            "tour",
            "tour_id",
        ]


class CreateOrderSerializer(serializers.ModelSerializer):
    tour_id = serializers.PrimaryKeyRelatedField(
        queryset=TourModel.objects.all(),
        source="tour"
    )

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "name",
            "phone",
            "quantity",
            "data",
            "comment",
            "tour_id",
        ]



    def create(self, validated_data):
        order = super().create(validated_data)

        request = self.context.get("request")
        if order.tour.image:
            if request:
                image_url = request.build_absolute_uri(order.tour.image.url)
            else:
                from django.conf import settings
                image_url = f"{order.tour.image.url}"
        else:
            image_url = None

        order_created_handler(order, image_url=image_url)

        return order
