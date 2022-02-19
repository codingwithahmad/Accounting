from django.db import models
from django.utils import timezone

# Create your models here.
class Sabt(models.Model):
    title = models.CharField(max_length=128)
    income = models.IntegerField()
    spending = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
