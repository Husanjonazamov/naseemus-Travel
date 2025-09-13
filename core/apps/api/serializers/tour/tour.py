from rest_framework import serializers

from core.apps.api.models import TourModel
from core.apps.api.serializers.category import  BaseCategorySerializer



class BaseTourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = BaseCategorySerializer()
    image_url = serializers.SerializerMethodField()

    
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
        
    def get_image_url(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url  
        
    def get_images(self, obj):
        from core.apps.api.serializers.tourimage import BaseTourimageSerializer
        request = self.context.get('request')
        return BaseTourimageSerializer(obj.images.all(), many=True, context={'request': request}).data



class ListTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class RetrieveTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


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
