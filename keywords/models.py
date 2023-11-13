from django.db import models


class Keyword(models.Model):
    entry = models.CharField(max_length=50, unique=True)
    products = models.ForeignKey(
        "products.Product", on_delete=models.PROTECT, related_name="keywords"
    )
