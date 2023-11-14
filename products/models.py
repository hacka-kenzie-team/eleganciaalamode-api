from django.db import models


# class Category(models.TextChoices):
# class Collection(models.TextChoices):


class Product(models.Model):
    name = models.CharField(max_length=127, unique=True)
    slug = models.SlugField(max_length=127, unique=True)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=30)
    visit_number = models.IntegerField(default=0)
    collection = models.CharField(max_length=100)
    sale = models.BooleanField(default=False)
    spotlight = models.BooleanField(default=False)
    # keywords
    style = models.OneToOneField(
        "product_styles.Product_style", on_delete=models.CASCADE
    )
    # product_comments
