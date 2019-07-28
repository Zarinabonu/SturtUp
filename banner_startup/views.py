from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import StartUpBanner

class BannerListView(ListView):
    template_name = 'Banner/banner.html'
    model = StartUpBanner
    context_object_name = 'banners'

class BannerCreteView(TemplateView):
    template_name = 'Banner/banner.html'

class BannerUpdateView(DetailView):
    template_name = 'Banner/banner.html' 
    model = StartUpBanner
    context_object_name = 'banner'   

def index(request):
    return render(request,'Landing/index.html')        

