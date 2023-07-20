from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashbord.as_view(), name='dashbord'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('user-cart/', views.user_cart, name='user_cart'),
    path('delete-order-item', views.delete_from_order_items, name='delete_order_item'),
    path('change-item-count', views.cheng_item_count, name='change_item_count'),
]
