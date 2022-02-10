from django.urls import path
from .views import Home, CreateSabt


app_name = "main"


urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create", CreateSabt.as_view(), name="CreateSabt")
]
