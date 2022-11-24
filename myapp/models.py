from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    interested = models.PositiveIntegerField(default=0)

    def refill(self):
        new_stock = float(self.stock) + 100
        return new_stock

    def __str__(self):
        return self.name

class Client(User):
    PROVINCE_CHOICES = [('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec'),]
    company = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province=models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)

    # def __str__(self):
    #     return self.User

class Order(models.Model):
    product = models.ForeignKey(Product, related_name = 'orders', on_delete=models.CASCADE)
    client =  models.ForeignKey(Client, related_name = 'orders', on_delete=models.CASCADE)
    num_units = models.PositiveIntegerField(default=100)
    order_status = [(0,'Order Cancelled'),(1, 'Order Placed'),(2, 'OrderShipped'),(3, 'Order Delivered'),]
    status_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.product

class Employee(models.Model):
    name = models.CharField(max_length=500)
    eid = models.PositiveIntegerField( default=0)
    status = models.CharField(max_length=500)
    department = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Empsin(models.Model):
    eid = models.CharField(max_length=500)
    sin = models.CharField(max_length=500)
    salary = models.CharField(max_length=500)

    def __str__(self):
        return self.eid

class login(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.username

class adminlogin(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.username





