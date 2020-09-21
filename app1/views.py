from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(request, username=username1, password=password1)
        
        
        if user is not None:
            if user.is_staff:
                auth_login(request, user)
                return redirect('app3/product_form_view/')
            else:
                auth_login(request, user)
                return redirect('app3/display_product/')


        else:
            messages.info(request, "username or password is incorrect")

            
    return render(request, 'login.html')


def logout(request):
        auth.logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("/")

def about_us(request):
    return render(request, "about_us.html")

def new_arrivals(request):
    return render(request, "new_arrivals.html")

def men(request):
    return render(request, "men.html")

def women(request):
    return render(request, "women.html")

def kids(request):
    return render(request, "kids.html")
