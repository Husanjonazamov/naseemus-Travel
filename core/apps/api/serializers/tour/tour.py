from rest_framework import serializers

from core.apps.api.models import TourModel
from core.apps.api.serializers.category import BaseCategorySerializer
from core.apps.api.serializers.sanatory import BaseSanatorySerializer


class BaseTourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    category = BaseCategorySerializer()
    is_liked = serializers.SerializerMethodField()


    class Meta:
        model = TourModel
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "price",
            "image",
            "date",
            "category",
            "is_popular",
            "is_new",
            "images",
            "maps",
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    def get_images(self, obj):
        from core.apps.api.serializers.tourimage import BaseTourimageSerializer
        request = self.context.get("request")
        return BaseTourimageSerializer(
            obj.images.all(), many=True, context={"request": request}
        ).data


    def get_is_liked(self, obj):
        from core.apps.accounts.models import UserLikeModel
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_authenticated:
            return UserLikeModel.objects.filter(user=request.user, tour=obj).exists()
        return False



class ListTourSerializer(BaseTourSerializer):
    """List uchun - images va maps yo'q"""
    class Meta(BaseTourSerializer.Meta):
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "price",
            "image",
            "date",
            "category",
            "is_popular",
            "is_new",
            "is_liked",
        ]



class RetrieveTourSerializer(BaseTourSerializer):
    """Detail uchun - images, maps va sanatories bilan"""
    sanatories = BaseSanatorySerializer(many=True, read_only=True)
    
    class Meta(BaseTourSerializer.Meta):
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "price",
            "image",
            "date",
            "category",
            "is_popular",
            "is_new",
            "images",
            "maps",
            "sanatories",
            "is_liked",
        ]



class CreateTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourModel
        fields = [
            "title",
            "slug",
            "description",
            "price",
            "date",
            "is_popular",
            "image",
        ]
