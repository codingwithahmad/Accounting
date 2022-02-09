from django.shortcuts import render
from .models import Sabt
from django.views.generic import View
# Create your views here.


class Home(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
