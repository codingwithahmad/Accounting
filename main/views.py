from django.shortcuts import render
from .models import Sabt
from django.urls import reverse
from django.views.generic import View, CreateView
# Create your views here.


class Home(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CreateSabt(CreateView):
    template_name = "main/create_sabt.html"
    model = Sabt
    fields = "__all__"

    def get_success_url(self):
        return reverse('main:Home')
