from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from .models import Informations



# Create your views here.

def MainPage(request):
    return render(request, 'Django_app/main_page.html')

def CatProduct(request):
    return render(request, 'Django_app/Cat_product.html')

def DogProduct(request):
   
    return render(request, 'Django_app/Dog_product.html')    

def Sale(request):
    
    if request.POST:
        First_name = request.POST['firstname']
        Last_name = request.POST['lastname']
        Email = request.POST['email']
        Address1 = request.POST['address1']
        Phone_number = request.POST['P_number']
        Product_id = request.POST.get('product_id', '')
        print("Product_id:", Product_id)
        models.Informations.objects.create(First_name = First_name, Last_name = Last_name, Email = Email, Phone_number = Phone_number, Address1 = Address1, Product_id=Product_id)
        return render(request, 'Django_app/main_page.html')

    else:
        return render(request, 'Django_app/sale.html')    


