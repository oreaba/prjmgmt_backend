from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'website/index.html'
    # template_name = 'static_frontapp/website/index.html'
    # template_name = 'static_frontapp/website/index.html'