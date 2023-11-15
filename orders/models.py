from django.db import models


class Order(models.Model):
    is_paid = models.BooleanField(default=True)
    date_paid = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="orders"
    )
    # items_bought ( order_items )
