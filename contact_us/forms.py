from django import forms

from contact_us.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'موضوع پیام'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیام'
            }),
        }
        labels = {
            'full_name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        error_messages = {
            'full_name': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'email': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'subject': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'message': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
        }
