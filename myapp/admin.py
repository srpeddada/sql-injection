from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, Category, Client, Order, Empsin, Employee, login, adminlogin
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Empsin)
admin.site.register(Employee)
admin.site.register(login)
admin.site.register(adminlogin)