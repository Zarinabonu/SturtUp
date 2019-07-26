from django.db import models

class StartUpRegister(models.Model):
    firstname = models.TextField(blank=True,default='')
    lastname = models.TextField(blank=True,default='')
    contact_email = models.TextField(blank=True,default='')
    contact_number = models.IntegerField(blank=True,default='')
    title = models.TextField(blank=True,default='')
    description = models.TextField(blank=True,default='')
    photo = models.ImageField(blank=True,null=True)
