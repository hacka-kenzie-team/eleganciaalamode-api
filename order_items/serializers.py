from rest_framework import serializers
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "order",
            "product_name",
            "product_price",
            "quantity"
        ]

        extra_kwargs = {
            "order": {"required": False},
        }
