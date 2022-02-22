from django.urls import path
from .views import Home, CreateSabt, AllSabt, Sabt


app_name = "main"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create", CreateSabt.as_view(), name="CreateSabt"),
    path("all", AllSabt.as_view(), name="AllSabt"),
    path("sabt/<int:pk>", Sabt.as_view(), name="Sabt"),
]
