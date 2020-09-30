from django.shortcuts import render
from django.db import models
from order.models import Pizza
from order.models import Customer
from order.models import PizzaPromo
from order.forms import PizzaForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse

#from account.forms import OrderForm
# Create your views here.


def index(request):
    
    pizzas = Pizza.objects.all()
    promos = PizzaPromo.objects.all()
    #form = PizzaForm()
    

    if request.is_ajax():
        email = request.POST.get('email-lg')
        password = request.POST.get('password-lg')
    
        user = Customer.objects.filter(email = email, password = password).exists()
        render(request, 'mainApp/index.html', {'pizzas':pizzas}, {'user': user},)
        if user is True:
            print("USER EXIST!")
            return JsonResponse({
                'msg': 'Success'
            })
        else:
            print("USER ERROR!")
            return JsonResponse({
                'msg': 'Error'
            })
        context = {
            'pizzas': pizzas,
            'user': user,
            #'promos': promos,
        }
        return render(request, 'mainApp/index.html', context)
    else:
       
        context = {
        'pizzas': pizzas,
        'user': False,
        #'promos': promos,
        }
        return render(request, 'mainApp/index.html', context)


def orderTracker(request):
    return render(request, 'mainApp/order-tracker.html')