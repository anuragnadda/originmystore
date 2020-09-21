
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email_id']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User is already exists")
                return redirect('signup')
        
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('signup')
            
            else:        
                user = User.objects.create_user(username=username, email=email, first_name=firstname,
                last_name=lastname, password=password1) 
                user.save()
                messages.info(request, "User created")
                return redirect('/')
        else:
            messages.info(request, "password not matching")
            return redirect('signup')
            
        return redirect("/")
  


    else:
        return render(request, "signup.html")


