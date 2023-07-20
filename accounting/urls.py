from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('referer-login/', views.RefereLoginView.as_view(), name='RefererLogin'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('forgetpass/', views.ForGetPassView.as_view(), name='forgetpass'),
    path('reset/', views.ResertPassView.as_view(), name='resetpass'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
