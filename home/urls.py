from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('header-login/', views.header_login, name='header_login'),
    # path('refrer-login/', views.referer_login, name='go_login'),
]
