from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="login"),
    path('new_arrivals/', views.new_arrivals, name="new_arrivals"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('kids/', views.kids, name="kids"),
    path('about_us/', views.about_us, name="about_us"),

    
]
