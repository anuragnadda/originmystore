from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.
def product_list(request):
    if request.method == 'GET': 
  
        # getting all the objects of product. 
        Products = Product.objects.all()  
        return render(request, 'viewcart.html',{'product_list' : Products})


  
def product_form_view(request): 
  
    if request.method == 'POST': 
        form = ProductForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ProductForm() 
    return render(request, 'productForm.html', {'form' : form}) 
  
  
def success(request): 
    return render(request, ('success.html'))


def display_product(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of product. 
        Products = Product.objects.all()  
        return render(request, 'product_list.html',{'product_list' : Products})

def add_to_cart(request):
    Products = Product.objects.get(pk=request.POST.get('productid'))
  
    return render(request, 'viewcart.html',{'Products':Products})
        

def address(request):
    if request.method == 'POST': 
        form = AddressForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('payment') 
    else: 
        form = AddressForm() 
    return render(request, 'address.html', {'form' : form}) 

def payment(request):
    if request.method == 'POST': 
        form = PaymentForm(request.POST,request.FILES)

        if form.is_valid(): 
            form.save()
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form' : form})


def thank_you(request):
    return render(request, 'thankyou.html')


