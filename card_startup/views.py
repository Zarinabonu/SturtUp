from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, View, TemplateView
from .models import StartUpCard

# def func(self,request):
#     return render(request,'dsdssda')
class CardListView(ListView):
    template_name = 'Card/card.html'
    model = StartUpCard
    context_object_name = 'cards'
