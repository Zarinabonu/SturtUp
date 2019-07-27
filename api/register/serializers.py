from rest_framework.serializers import ModelSerializer
from register_startup.models import StartUpRegister

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = StartUpRegister
        fields = (
            'firstname',
            'lastname' ,
            'contact_info',
            'title' ,
            'description' ,
            'photo'
            )