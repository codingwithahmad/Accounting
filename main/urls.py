from django.urls import path
from .views import Home, CreateSabt, AllSabt


app_name = "main"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create", CreateSabt.as_view(), name="CreateSabt"),
    path("all", AllSabt.as_view(), name="AllSabt"),
]
