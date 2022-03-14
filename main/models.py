from django.db import models
from django.utils import timezone
from user.models import User

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
    author = models.ForeignKey(User, related_name="sabts", on_delete=models.CASCADE)


    def __str__(self):
        return self.title + "_" + self.author
