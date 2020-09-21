from django import forms 
from .models import *
  
class ProductForm(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['name','quantity','description','price','image'] 

class AddressForm(forms.ModelForm): 
  
    class Meta: 
        model = ShippingAddress 
        fields = ['user','order','address','city','state','phonenumber','pincode'] 

class PaymentForm(forms.ModelForm): 
   
    class Meta: 
        model = Payment
        fields = ['name','cardnumber','expiration','cvv'] 