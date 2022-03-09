from django.urls import path
from .views import (Home,
    create_sabt,
    get_categories,
    CreateCategory,
    AllSabt,
    Sabt,
    CategorySabts,
    ModifySabt,
    ListSabtAPIView,
    RetrieveSabtAPIView,
)


app_name = "main"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create/sabt", create_sabt, name="CreateSabt"),
    path("create/category", CreateCategory.as_view(), name="CreateCategory"),
    path("list/all", AllSabt.as_view(), name="AllSabt"),
    path("list/category/<slug:slug>", CategorySabts.as_view(), name="CategorySabts"),
    path("sabt/<int:pk>", Sabt.as_view(), name="Sabt"),
    path("sabt/update/<int:pk>", ModifySabt.as_view(), name="ModifySabt"),


    # API urls

    path("api/sabts", ListSabtAPIView.as_view(), name="api_sabts_list"),
    path("api/sabts/<int:pk>", RetrieveSabtAPIView.as_view(), name="api_sabts_retrieve"),
    path("api/categories", get_categories, name="api_categories_list"),
]
