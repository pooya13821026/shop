from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from shop.models import *
from site_setting.models import *


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['slider'] = Slider.objects.filter(is_active=True)
        context['newset_products'] = ProductList.objects.filter(is_active=True, is_delete=False).order_by(
            '-create_date')[:8]
        more_view_product = ProductList.objects.filter(is_active=True, is_delete=False).annotate(
            view_count=Count('seenproduct')).order_by('-view_count')[:8]
        context['more_view_product'] = more_view_product
        context['baner'] = Baner.objects.filter(is_delete=False)
        context['banerbig'] = BanerBIg.objects.filter(is_delete=False)
        return context


def header(request):
    site_setting = SiteSetting.objects.filter(main_setting=True).first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'sheard/header.html', context)


def footer(request):
    site_setting = SiteSetting.objects.filter(main_setting=True).first()
    footer_title = FooterTital.objects.all()
    for item in footer_title:
        item.footerlink_set
    context = {
        'site_setting': site_setting,
        'footer_title': footer_title
    }
    return render(request, 'sheard/footer.html', context)


# def header_login(request):
#     url = request.META.get('HTTP_REFERER')
#     request.session['last_url'] = url
#     return redirect('RefererLogin')
#
#
# def referer_login(request):
#     url = request.META.get('HTTP_REFERER')
#     request.session['last_url'] = url
#     return redirect('RefererLogin')


