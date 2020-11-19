from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='files', blank=True)
    mtn = models.CharField(max_length=3)
    vodafone = models.CharField(max_length=3)
    glo = models.CharField(max_length=3)
    airtelTigo = models.CharField(max_length=3)


    