from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from contact_us.forms import ContactUsForm
from site_setting.models import SiteSetting


class ContactUsView(View):
    def get(self, request):
        contact_us_form = ContactUsForm
        site_setting = SiteSetting.objects.filter(main_setting=True)
        context = {
            'site_setting': site_setting,
            'contact_form': contact_us_form,
        }
        return render(request, 'contact_us/contact_us.html', context)

    def post(self, request):
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('home'))
