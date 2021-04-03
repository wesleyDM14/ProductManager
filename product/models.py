from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    validity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
