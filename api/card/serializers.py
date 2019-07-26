from rest_framework.serializers import ModelSerializer
from card_startup.models import StartUpCard

class CardSerializer(ModelSerializer):
    class Meta:
        model = StartUpCard
        fields = ('text', 'title', 'image')