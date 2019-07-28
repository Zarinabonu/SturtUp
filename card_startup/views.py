from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, View, TemplateView ,DetailView
from .models import StartUpCard


class CardListView(ListView):
    template_name = 'Card/card.html'
    model = StartUpCard
    context_object_name = 'cards'

class CardCreateView(TemplateView):
    template_name = 'Card/card.html'  

class CardUpdateView(DetailView):
    template_name = 'Card/card.html' 
    model = StartUpCard 
    context_name = 'card'    
