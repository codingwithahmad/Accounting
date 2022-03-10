from django.shortcuts import render, get_object_or_404
from .models import Sabt as Sabt_model, Category
from django.urls import reverse
from main.forms import SabtForm
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SabtSerializer, CategorySerializer

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
    model = Sabt_model


class CategorySabts(ListView):
    template_name = "main/category_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.sabts.all()


class Sabt(DetailView):
    template_name = "main/sabt_details.html"
    model = Sabt_model


class ModifySabt(UpdateView):
    template_name = "main/modify_sabt.html"
    model = Sabt
    form_class = SabtForm

    def get_queryset(self):
        sabt_id = self.kwargs.get('id')
        sabt = get_object_or_404(Sabt.objects.get(pk=sabt_id))
        return sabt

# API views

class ListSabtAPIView(ListAPIView):
    queryset = Sabt_model.objects.all()
    serializer_class = SabtSerializer

class RetrieveSabtAPIView(RetrieveAPIView):
    queryset = Sabt_model.objects.all()
    serializer_class = SabtSerializer
    lookup_fields = ['id']

@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_categories(request):
    """

    List all categories
    """
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def get_category(request, pk):
    """

    Retrieve api view for show on category with pk
    """

    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse(data={"message": "There is no category with this id"}, status=404)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly, ))
def create_category(request):
    """

    Create view for category model
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.error, status=400)
