from django.shortcuts import render, get_object_or_404
from .models import Sabt, Category
from django.urls import reverse
from main.forms import SabtForm
from django.views.generic import View, CreateView, ListView, DetailView
# Create your views here.


class Home(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def create_sabt(request):
    if request.method == 'POST':
        form = SabtForm(request.POST)
        if form.is_valid():
            n_sabt = form.save()
            categories = request.POST.getlist('cats')
            for cat in categories:
                n_sabt.category.add(cat)

            return render(request, 'main/home.html')

        return render(request, 'main/create_sabt.html', {'form': SabtForm})

    return render(request, 'main/create_sabt.html', {'form': SabtForm})

class CreateCategory(CreateView):
    template_name = "main/create_cats.html"
    model = Category
    fields = ['title', 'slug', 'parent']

    def get_success_url(self):
        return reverse('main:Home')

class AllSabt(ListView):
    template_name = "main/all_sabt.html"
    model = Sabt


class CategorySabts(ListView):
    template_name = "main/category_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.sabts.all()


class Sabt(DetailView):
    template_name = "main/sabt_details.html"
    model = Sabt
