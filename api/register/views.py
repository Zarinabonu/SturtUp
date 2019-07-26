from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from register_startup.models import StartUpRegister
from .serializers import RegisterSerializer

class RegisterCreate(CreateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterSerializer
    

class RegisterUpdate(UpdateAPIView):
    queryset = StartUpRegister.objects.all()
    serializer_class = RegisterSerializer
    lookup_url_kwargs = 'id'

class RegisterDelete(DestroyAPIView):
    queryset =  StartUpRegister.objects.all()
    lookup_url_kwargs ='id'   
