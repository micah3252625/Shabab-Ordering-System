from django.db import models
import decimal
from decimal import Decimal
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Customer(models.Model):
    SALUTATION = (
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
    )
    #Personal Information
    salutation = models.CharField(max_length=10, null=True, choices=SALUTATION, default='Mr.')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    
    #Location
    street = models.CharField(max_length=150, null=True)
    barangay = models.CharField(max_length=150, null=True)

    #Contact Details
    number = models.CharField(max_length=20, null=True)

    #Email Address
    email = models.EmailField(max_length = 254, null=True)

    #Password
    password = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.salutation + " " + self.first_name + " " + self.last_name + " | " + self.email

class PizzaPromo(models.Model):
    image = models.ImageField(upload_to='account/images/', null=True)
    promo_name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return "PROMO: " + self.promo_name
        
class Pizza(models.Model):
    SIZE = (
        (8, 8),
        (10, 10),
        (12, 12),
    )
    size = models.IntegerField(null=True, choices=SIZE, default='8')
    name = models.CharField(max_length=100)

    base_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    image = models.ImageField(upload_to='account/images/', null=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Order Pending', 'Order Pending'), 
        ('Order Preparing', 'Order Preparing'),
        ('Order on its way', 'Order on its way'),
        )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizzas = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Order Submitted')
    
    def __str__(self):
        return "Order By: " + self.customer.first_name + " " + self.customer.last_name

