from django.db import models

# Create your models here.
class Sabt(models.Model):
    title = models.CharField(max_length=128)
    inconme = models.IntegerField()
    spending = models.IntegerField()
