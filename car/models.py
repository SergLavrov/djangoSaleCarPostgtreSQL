from django.db import models

# Create your models here.

class Auto(models.Model):
    car_brand = models.CharField(max_length=30)
    year_production = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=25)


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product_count = models.IntegerField()
    price = models.IntegerField()
    # product_id = models.IntegerField()
    # customer_id = models.IntegerField()
