from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from card_startup.models import StartUpCard
from .serializers import CardSerializer , CardSerializer

class CardCreate(CreateAPIView):
    queryset = StartUpCard.objects.all()
    serializer_class = CardSerializer

class CardUpdate(UpdateAPIView):
     queryset = StartUpCard.objects.all()
     serializer_class = CardSerializer
     lookup_url_kwarg = 'id'  

class CardDelete(DestroyAPIView):
    queryset = StartUpCard.objects.all()
    lookup_url_kwargs = 'id'      

    