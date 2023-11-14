from rest_framework import serializers
from .models import Product_style


class ProductStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_style
        fields = [
            "url"
        ]
