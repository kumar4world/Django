from django.db import models

# Create your models here.
class Spanish(models.Model):
    english = models.CharField(max_length=200)
    spanish = models.CharField(max_length=200)
    others =  models.CharField(max_length=200, default='0000000')
