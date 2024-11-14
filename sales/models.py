from django.db import models

class Sale(models.Model):
    purchase_order = models.CharField(max_length=100, unique=True)
    date_of_purchase = models.DateTimeField()
    customer_id = models.CharField(max_length=50)
    item_code = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.purchase_order} - Customer {self.customer_id}"