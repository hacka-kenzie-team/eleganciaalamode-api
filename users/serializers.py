from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "name",
            "password",
            "is_superuser",
            "orders",
            "comments",
        ]
        depth = 1
        extra_kwargs = {
            "password": {'write_only': True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="user with this email already exists.",
                    )
                ],
            },
            "is_superuser": {"default": False},
            "orders": {
                "read_only": True,
                "many": True
            },
            "comments": {
                "read_only": True,
                "many": True,
                "source": "user_comments"
            },
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
