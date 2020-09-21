
from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.product_list, name="products"),
    path('product_form_view/', views.product_form_view, name= "product_form_view"),
    path('success/', views.success, name = 'success'),
    path('display_product/', views.display_product, name="displayproduct"),
    path('add_to_cart/', views.add_to_cart, name="addtocart"),
    path('address/', views.address, name="address"),
    path('payment/', views.payment, name="payment"),
    path('thank_you/', views.thank_you, name="thank_you"),
]
