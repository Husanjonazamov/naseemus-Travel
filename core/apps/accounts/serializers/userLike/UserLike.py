from rest_framework import serializers

from core.apps.accounts.models import UserLikeModel
from core.apps.api.models import TourModel


class BaseUserLikeSerializer(serializers.ModelSerializer):
    tour_title = serializers.CharField(source="tour.title", read_only=True)
    tour_slug = serializers.CharField(source="tour.slug", read_only=True)
    tour_image = serializers.ImageField(source="tour.image", read_only=True)

    class Meta:
        model = UserLikeModel
        fields = [
            "id",
            "tour_title",
            "tour_slug",
            "tour_image",
            "created_at",
        ]


class ListUserLikeSerializer(BaseUserLikeSerializer):
    tour = serializers.SerializerMethodField()

    class Meta(BaseUserLikeSerializer.Meta):
        fields = [
            "id",
            "tour",
            "created_at",
        ]

    def get_tour(self, obj):
        from core.apps.api.serializers.tour.tour import ListTourSerializer
        return ListTourSerializer(obj.tour, context=self.context).data



class CreateUserLikeSerializer(serializers.Serializer):

    tour_slug = serializers.SlugField()

    def validate_tour_slug(self, value):
        if not TourModel.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Tur topilmadi")
        return value

