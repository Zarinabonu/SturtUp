from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import StartUpRegister
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

class RegisterCreateList(ListView):
    template_name = 'Inbox/inbox.html' 
    model = StartUpRegister
    context_name = 'registers'

class RegisterCreateView(TemplateView):
    template_name = 'Inbox/inbox.html'

class RegisterUpdateView(DetailView):
    template_name = 'Inbox/inbox.html'
    model = StartUpRegister
    context_name = 'regsiter'

# def index(request):
#     send_mail('Hello Email',
#     'First Email connection',
#     'zarinabonu779@gmail.com',
#     ['zarinabonu199924@gmail.com'],
#     fail_silently=False)
#     return render(request, 'Inbox/inbox.html')

# #  your views here.
