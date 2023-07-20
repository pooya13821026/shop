from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput())
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='تکرار گذرواژه', widget=forms.PasswordInput())
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            return ValidationError('کلمه عبور وارد شده با تکرار ان مطابقت ندارد')


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput())
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput())


class ForGetPassForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput())


class ResetForm(forms.Form):
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='تکرار گذرواژه', widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            return ValidationError('کلمه عبور وارد شده با تکرار ان مطابقت ندارد')
