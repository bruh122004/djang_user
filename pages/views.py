from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
#this class just displays a template by providing its name
class HomePageView(TemplateView):
    template_name='home.html'