from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "rating",
            "product_name",
            "user_name"
        ]
        read_only_fields = ["product_name", "user_name"]

    def get_product_name(self, obj):
        return obj.product_name.name

    def get_user_name(self, obj):
        return obj.user_name.name
