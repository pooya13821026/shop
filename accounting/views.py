from django.contrib.auth import login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounting.forms import *
from accounting.models import MyUser


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm
        context = {
            'register': register_form
        }
        return render(request, 'accounting/sing up.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashbord'))
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('username')
            user_pass = register_form.cleaned_data.get('password')
            user_email = register_form.cleaned_data.get('email')
            user: bool = MyUser.objects.filter(username__iexact=user_name).exists()
            if user:
                register_form.add_error('username', 'این نام کلربری تکراری میباشید')
                register_form.add_error('moblie', 'این شماره تکراری میباشید')
            else:
                registered_form = MyUser(email=user_email, password=user_pass, username=user_name)
                registered_form.set_password(user_pass)
                login(request, user)
                registered_form.save()
            return redirect(reverse('home'))
        context = {
            'register': register_form,
        }
        return render(request, 'accounting/sing up.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm
        context = {
            'login': login_form
        }
        return render(request, 'accounting/sing in.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashbord'))
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name_user = login_form.cleaned_data.get('username')
            pass_user = login_form.cleaned_data.get('password')
            user: MyUser = MyUser.objects.filter(username__iexact=name_user).first()
            if user is not None:
                if user.is_active:
                    ckeck_pass = user.check_password(pass_user)
                    if ckeck_pass:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('password', 'گذرواژه اشتباه است')
                else:
                    login_form.add_error('username', 'این حساب فعال نمی باشد')
            else:
                login_form.add_error('username', 'حسابی با این مشخصات پیدا نشد')
        context = {
            'login': login_form,
        }
        return render(request, 'accounting/sing in.html', context)


class ForGetPassView(View):
    def get(self, request):
        forget_pass = ForGetPassForm()
        context = {
            'forget_pass': forget_pass,
        }
        return render(request, 'accounting/forgetpass.html', context)

    def post(self, request: HttpRequest):
        forget_pass = ForGetPassForm(request.POST)
        if forget_pass.is_valid():
            user_name = forget_pass.cleaned_data.get('username')
            user: MyUser = MyUser.objects.filter(username__iexact=user_name).first()
            if user is not None:
                return redirect(reverse('resetpass'))
            else:
                forget_pass.add_error('username', 'کاربری به این نام وجود ندارد')
        context = {
            'forget_pass': forget_pass
        }
        return render(request, 'accounting/forgetpass.html', context)


class ResertPassView(View):
    def get(self, request):
        reset_pass = ResetForm()
        context = {
            'reset_pass': reset_pass
        }
        return render(request, 'accounting/resetpass.html', context)

    def post(self, request: HttpRequest):
        reset_pass = ResetForm(request.POST)
        user: MyUser = MyUser()
        if reset_pass.is_valid():
            user_pass = reset_pass.cleaned_data.get('password')
            user.set_password(user_pass)
            user.save()
            return redirect(reverse('login'))
        context = {
            'reset_pass': reset_pass
        }
        return render(request, 'accounting/resetpass.html', context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


# class RefereLoginView(View):
#     def get(self, request):
#         login_form = LoginForm
#         context = {
#             'login': login_form
#         }
#         return render(request, 'accounting/sing in.html', context)
#
#     def post(self, request: HttpRequest):
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             name_user = login_form.cleaned_data.get('username')
#             pass_user = login_form.cleaned_data.get('password')
#             user: MyUser = MyUser.objects.filter(username__iexact=name_user).first()
#             if user is not None:
#                 if user.is_active:
#                     ckeck_pass = user.check_password(pass_user)
#                     if ckeck_pass:
#                         login(request, user)
#                         url = request.session['last_url']
#                         return redirect(url)
#                     else:
#                         login_form.add_error('password', 'گذرواژه اشتباه است')
#                 else:
#                     login_form.add_error('username', 'این حساب فعال نمی باشد')
#             else:
#                 login_form.add_error('username', 'حسابی با این مشخصات پیدا نشد')
#         context = {
#             'login': login_form,
#         }
#         return render(request, 'accounting/sing in.html', context)
