from django.urls import path

from . import views

urlpatterns = [
    path('add-product-order', views.add_product, name='add_product_order'),
]
