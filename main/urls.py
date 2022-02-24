from django.urls import path
from .views import Home, CreateSabt, CreateCategory, AllSabt, Sabt


app_name = "main"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create/sabt", CreateSabt.as_view(), name="CreateSabt"),
    path("create/category", CreateCategory.as_view(), name="CreateCategory"),
    path("all", AllSabt.as_view(), name="AllSabt"),
    path("sabt/<int:pk>", Sabt.as_view(), name="Sabt"),
]
