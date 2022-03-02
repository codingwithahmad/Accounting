from django.urls import path
from .views import Home, create_sabt, CreateCategory, AllSabt, Sabt, CategorySabts


app_name = "main"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create/sabt", create_sabt, name="CreateSabt"),
    path("create/category", CreateCategory.as_view(), name="CreateCategory"),
    path("list/all", AllSabt.as_view(), name="AllSabt"),
    path("list/category/<slug:category>", CategorySabts.as_view(), name="CategorySabts"),
    path("sabt/<int:pk>", Sabt.as_view(), name="Sabt"),
]
