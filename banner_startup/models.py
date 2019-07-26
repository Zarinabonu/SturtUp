from django.db import models

class StartUpBanner(models.Model):
    image = models.ImageField(blank=True,null=True)
    title = models.TextField(blank=True,default='')
    info = models.TextField(blank=True,default='')

# Create your models here.
