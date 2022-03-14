from main.models import Sabt as Sabt_model, Category

from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SabtSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class ListSabtAPIView(ListAPIView):
    """

    List of Sabts
    """
    queryset = Sabt_model.objects.all()
    serializer_class = SabtSerializer

class RetrieveSabtAPIView(RetrieveAPIView):
    """

    Return a Sabt object with specific id
    """
    queryset = Sabt_model.objects.all()
    serializer_class = SabtSerializer
    lookup_fields = ['id']
    permission_classes = [IsAuthorOrReadOnly]

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly, ))
def create_sabt(request):
    """

    This view just receive POST request and if request body is valid,
    it's save new sabt in db
    """
    try:
        data = JSONParser().parse(request)
        serializer = SabtSerializer(data=data)
        if serializer.is_valid():
            new_sabt = serializer.save()

        for cat in data.get("category"):
            new_sabt.category.add(cat)

        return JsonResponse(serializer.data, status=201)
    except Exception as e:
        return JsonResponse({"message": f"{e}"}, status=400)

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
