from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product
from keywords.models import Keyword
from product_styles.models import Product_style
from product_styles.serializers import ProductStyleSerializer
from keywords.serializers import KeywordSerializer
from comments.serializers import CommentSerializer


class ProductSerializer(serializers.ModelSerializer):
    style = ProductStyleSerializer()
    keywords = KeywordSerializer(many=True)
    comments = CommentSerializer(
        source='comment_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "stock",
            "description",
            "category",
            "visit_number",
            "collection",
            "sale",
            "spotlight",
            "keywords",
            "style",
            "comments"
        ]
        depth = 1
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Product.objects.all(),
                        message="A product with that name already exists.",
                    )
                ],
            },
            "slug": {
                "validators": [
                    UniqueValidator(
                        queryset=Product.objects.all(),
                        message="slug for that name already exists.",
                    )
                ],
                "required": {False}
            },
            "comments": {
                "read_only": True,
                "many": True,
                "source": "product_comments"
            },
        }

    def create(self, validated_data: dict):
        keyword_list = Keyword.objects.all()
        keywords = validated_data.pop("keywords")
        style_data = validated_data.pop("style")
        style = Product_style(**style_data)
        style.save()
        product = Product.objects.create(**validated_data, style=style)
        for instance in keywords:
            if instance not in keyword_list.values("entry"):
                new_keyword = Keyword.objects.create(**instance)
                product.keywords.add(new_keyword)
            else:
                reused_keyword = Keyword.objects.get(entry=instance["entry"])
                product.keywords.add(reused_keyword)

        return product

    def update(self, instance: Product, validated_data: dict) -> Product:
        keyword_list = Keyword.objects.all()
        keywords = validated_data.pop("keywords", None)
        if keywords is not None:
            new_keywords = []
            for item in keywords:
                if item not in keyword_list.values("entry"):
                    new_keyword = Keyword.objects.create(**item)
                    new_keywords.append(new_keyword)
                else:
                    reused_keyword = Keyword.objects.get(
                        entry=item["entry"]
                    )
                    new_keywords.append(reused_keyword)
            instance.keywords.set(new_keywords)

        style_data = validated_data.pop("style", None)
        if style_data is not None:
            style = Product_style(**style_data)
            style.save()
            instance.style = style
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
