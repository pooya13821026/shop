from django.shortcuts import render
from django.views.generic import ListView
from about.models import About


class AboutView(ListView):
    model = About
    template_name = 'about/about.html'
