from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    name = models.CharField(max_length=127)
    # username
    # is_superuser
    # password

    # orders
    user_comments = models.ManyToManyField(
        Product, through="comments.Comment", related_name="product_comments")
