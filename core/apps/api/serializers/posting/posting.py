from rest_framework import serializers

from core.apps.api.models import PostingTypeModel
from core.apps.api.serializers.feature import BaseFeatureSerializer

class BasePostingTypeSerializer(serializers.ModelSerializer):
    feature = serializers.SerializerMethodField()
    
    class Meta:
        model = PostingTypeModel
        fields = [
            "id",
            "title",
            "price",
            "feature",
        ]
        
    def get_feature(self, obj):
        return BaseFeatureSerializer(obj.feature, many=True).data


class ListPostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta): ...


class RetrievePostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta): ...


class CreatePostingTypeSerializer(BasePostingTypeSerializer):
    class Meta(BasePostingTypeSerializer.Meta):
        fields = [
            "id",
            "title",
            "price",
            "feature",
        ]
