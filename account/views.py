from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from account.forms import RegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from order.models import Customer

# Create your views here.
def register(request):
    form = RegistrationForm()
    form_error = False
    
    context = {
        'form': form,
        'form_error': form_error,
    }
   
    if request.is_ajax():
        form = RegistrationForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })
        else:
            return JsonResponse({
                'msg': 'Error'
            })

    else:
        form = RegistrationForm()
        form_error = True
    
    return render(request, 'register.html', context)

    '''
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            print("FORM IS VALID")
            messages.success(request, 'Successful!')
            register_form.save()
            return redirect('index')
        else:
            print("FORM IS NOT VALID")
            messages.error(request, 'Error!')
            form_error = True
            return redirect('register')
    else:
        form = RegistrationForm()
        form_error = True
    '''
   
  
  

    '''
        salutation=request.POST.get("salutation")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        street=request.POST.get("street")
        barangay=request.POST.get("barangay")
        number=request.POST.get("number")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        if password != confirm_password:
            print("PASSWORD UNMATCH!")
            return redirect('register')
        else:
            Customer.objects.create(salutation=salutation, first_name=first_name, last_name=last_name, street=street, barangay=barangay, number=number, email=email, password=password)
            return redirect('index')
        '''
        #if u is not None:
        #register_form.save()
    '''
    if request.is_ajax():
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })
    '''