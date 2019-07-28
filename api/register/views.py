from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from register_startup.models import StartUpRegister
from .serializers import RegisterSerializer
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.conf import settings

class RegisterCreate(CreateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterSerializer

    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['ergash1994@gmail.com'],
        fail_silently=True,
    )
    

class RegisterUpdate(UpdateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterSerializer
    lookup_url_kwargs = 'id'

class RegisterDelete(DestroyAPIView):
    queryset =  StartUpRegister.objects.all()
    lookup_url_kwargs ='id'   
