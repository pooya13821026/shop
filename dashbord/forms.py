from django import forms

from accounting.models import MyUser


class EditProfileForms(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'moblie', 'bio']
        widgets = {
            'fist_name': forms.TextInput(attrs={
                'placeholder': 'نام',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'نام خانوادگی',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control'
            }),
            'moblie': forms.NumberInput(attrs={
                'placeholder': 'شماره تماس',
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'بیو گرافی',
                'class': 'form-control',
                'rows': 3
            }),
        }


class DiscountForm(forms.Form):
    code = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد تخفیف خود را وارد کنید'
        })
    )
