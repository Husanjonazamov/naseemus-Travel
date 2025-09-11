from rest_framework import serializers

from core.apps.api.models import BlogModel


class BaseBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = [
            "id",
            "title",
            "description",
            "image"
        ]


class ListBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class RetrieveBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class CreateBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta):
        fields = [
            "id",
             "title",
            "description",
            "image"
        ]
