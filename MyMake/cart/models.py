from django.db import models
from products.models import Products

from resources.base import BaseModel
from customers.models import Customer

# Create your models here.
class Carts(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    products = models.JSONField()
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f" Carrinho de {self.customer}"

    def __repr__(self):
        return f"{self.id}"
