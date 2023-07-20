from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('category/<str:category>', views.ProductListView.as_view(), name='product_category'),
    path('product/<str:slug>', views.ProductDeteilView.as_view(), name='product_deteil'),
    path('send-comment/', views.send_comment_product, name='send_comment'),
    path('brand/<br>', views.ProductListView.as_view(), name='product_brand_list'),
    path('like/<int:id>/', views.product_like, name='product_like'),
    path('dislike/<int:id>/', views.product_dislike, name='product_dislike'),
    path('search/', views.search, name='search'),
]
