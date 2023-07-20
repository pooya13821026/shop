from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('send-comment/', views.send_comment, name='send_comment'),
    path('<str:slug>', views.BlogDeteliView.as_view(), name='blog_deteil'),
    path('categorys/<str:categorys>', views.BlogListView.as_view(), name='blog_category'),
]
