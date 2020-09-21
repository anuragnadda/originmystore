from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model): 
        name = models.CharField(max_length=100) 
        quantity = models.CharField(max_length=30)
        description = models.CharField(max_length=200)
        price = models.FloatField()
        image = models.ImageField(upload_to='images/') 

        def __str__(self):
                return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank= False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0, null=True ,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class Payment(models.Model):
    name = models.CharField(max_length=100) 
    cardnumber = models.CharField(max_length=12)
    expiration = models.CharField(max_length=8)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)



