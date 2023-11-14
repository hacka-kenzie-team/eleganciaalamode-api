from rest_framework import serializers
from .models import Order
from order_items.models import OrderItem
from order_items.serializers import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items_bought = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "user_id",
            "is_paid",
            "date_paid",
            "items_bought"
        ]

        extra_kwargs = {
            "date_paid": {"read_only": True},
            "user": {"required": False, "source": "user"}
        }

    def create(self, validated_data: dict):
        items_bought = validated_data.pop("items_bought")
        order = Order.objects.create(**validated_data)
        for instance in items_bought:
            OrderItem.objects.create(**instance, order=order)

        return order
