from django.urls import path
from mebel.views import home, products, productdetail, about, contact 

urlpatterns = [
        path('', home, name='home'),
        path('about-us/', about, name='about-us'),
        path('products/', products, name='products'),
        path('contact/', contact, name='contact'),
        path('product/<int:pk>', productdetail, name='product-detail'),

        ]
