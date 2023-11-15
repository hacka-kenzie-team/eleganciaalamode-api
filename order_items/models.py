from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="items_bought"
    )
    product_name = models.CharField(max_length=127)
    product_price = models.FloatField()
    quantity = models.IntegerField()
