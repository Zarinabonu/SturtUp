from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from banner_startup.models import StartUpBanner
from .serializers import BannerSerializer

class Banner_Create(CreateAPIView):
    queryset = StartUpBanner.objects.all()
    serializer_class = BannerSerializer

class Banner_Update(UpdateAPIView):
    queryset = StartUpBanner.objects.all()
    serializer_class = BannerSerializer
    lookup_url_kwargs = 'id'

class Banner_Delete(DestroyAPIView):
    queryset = StartUpBanner.objects.all()
    lookup_url_kwargs ='id'       