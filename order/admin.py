from django.contrib import admin
from order.models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(PizzaPromo)