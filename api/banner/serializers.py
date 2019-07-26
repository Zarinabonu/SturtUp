from rest_framework.serializers import ModelSerializer
from banner_startup.models import StartUpBanner

class BannerSerializer(ModelSerializer):
    class Meta:
        model = StartUpBanner
        fields = ('info', 'title', 'image')