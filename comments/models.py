from django.db import models
from users.models import User
from products.models import Product


class Comment(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    product_name = models.ForeignKey(Product, on_delete=models.PROTECT)
    user_name = models.ForeignKey(User, on_delete=models.PROTECT)
