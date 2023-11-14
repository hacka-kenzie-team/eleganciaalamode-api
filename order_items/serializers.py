from rest_framework import serializers
from .models import OrderItem
# from products.models import Product


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
            # "product_price": {"read_only": True},
        }

    # def create(self, validated_data):
    #     product = Product.objects.filter(
    #         name=validated_data["product_name"]
    #     )
    #     if product:
    #         validated_data["product_price"] = product.values()["price"]
    #     else:
    #         raise serializers.ValidationError(
    #             f'Product {validated_data["product_name"]} was not found.'
    #         )

    #     return OrderItem.objects.create(**validated_data)
