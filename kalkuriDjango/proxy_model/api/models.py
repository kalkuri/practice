
from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductProxy(Product):
    class Meta:
        proxy = True

    def discounted_price(self):
        return self.price * Decimal('0.90')
