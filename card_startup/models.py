from django.db import models

class StartUpCard(models.Model):
    text = models.TextField(blank=True,default='')
    title = models.TextField(blank=True,default='')
    image = models.ImageField(blank=True,default='')

# Create your models here.
