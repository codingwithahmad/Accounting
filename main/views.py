from django.shortcuts import render
from .models import Sabt, Category
from django.urls import reverse
from main.forms import SabtForm
from django.views.generic import View, CreateView, ListView, DetailView
# Create your views here.


class Home(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CreateSabt(CreateView):
    template_name = "main/create_sabt.html"
    form_class = SabtForm

    def get_success_url(self):
        return reverse('main:Home')


class CreateCategory(CreateView):
    template_name = "main/create_cats.html"
    model = Category
    fields = ['title', 'slug', 'parent']

    def get_success_url(self):
        return reverse('main:Home')

class AllSabt(ListView):
    template_name = "main/all_sabt.html"
    model = Sabt


class Sabt(DetailView):
    template_name = "main/sabt_details.html"
    model = Sabt
