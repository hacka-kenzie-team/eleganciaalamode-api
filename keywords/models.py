from django.db import models


class Keyword(models.Model):
    entry = models.CharField(max_length=50)
    products = models.ManyToManyField(
        "products.Product", related_name="keywords"
    )
