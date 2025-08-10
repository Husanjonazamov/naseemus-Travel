from rest_framework import serializers
from payme import Payme
from config.env import env

from core.apps.api.models import ListingModel, PostingTypeModel

PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")


class BaseListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields = [
            "id",
            "address",
            "full_name",
            "contact_time",
            "category",
            "posting_type",
            "specialty",
            "price",
            "age",
            "bio",
            "phone",
            "telegram",
            "image"
        ]


class ListListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...


class RetrieveListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta): ...

class CreateListingSerializer(BaseListingSerializer):
    class Meta(BaseListingSerializer.Meta):
        fields = [
            "id",
            "address",
            "full_name",
            "contact_time",
            "category",
            "posting_type",
            "specialty",
            "price",
            "age",
            "bio",
            "phone",
            "telegram",
            "image",
        ]

    def create(self, validated_data):
        posting_type = validated_data.get("posting_type")

        posting_type_obj = PostingTypeModel.objects.get(id=posting_type.id)

        listing = ListingModel.objects.create(**validated_data)

        price = int(posting_type_obj.price * 100)
        order_id = posting_type_obj.id  

        payme = Payme(merchant_id=PAYME_ID, key=PAYME_KEY)
        pay_link = payme.initializer.generate_pay_link(
            id=order_id,
            amount=price,
            return_url=""  
        )

        listing.payme_link = pay_link

        return listing

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["pay_link"] = getattr(instance, "payme_link", None)
        return data
