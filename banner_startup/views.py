from django.shortcuts import render
from ddjango.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TeplateView, ListView, View, DetailView
from .models import StartUpBanner

class BannerListView(ListView):
    template_name = ''
    model = StartUpBanner
    context_object_name = 'banners'

 class BannerCreateView(TemplateView):
     template_name = ''

 class RegisterUpdateView(DetailView):
     template_name = ''
     model = StartUpRegister
     context_object_name = 'banners'       
# Create your views here.
