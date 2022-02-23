from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True,
                               on_delete=models.SET_NULL,
                               related_name='children')
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Sabt(models.Model):
    title = models.CharField(max_length=128)
    income = models.IntegerField()
    spending = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="sabts")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
