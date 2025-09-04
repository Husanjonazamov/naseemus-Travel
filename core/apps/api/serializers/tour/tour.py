from rest_framework import serializers

from core.apps.api.models import TourModel



class BaseTourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = TourModel
        fields = [
            "id",
            "title",
            "description",
            "price",
            "image",
            "date",
            "is_popular",
            "is_new",
            "images"
        ]
        
    def get_images(self, obj):
        from core.apps.api.serializers.tourimage import BaseTourimageSerializer
        request = self.context.get('request')
        return BaseTourimageSerializer(obj.images.all(), many=True, context={'request': request}).data



class ListTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class RetrieveTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta): ...


class CreateTourSerializer(BaseTourSerializer):
    class Meta(BaseTourSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
