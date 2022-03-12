from django.urls import path
from .views import (
    create_sabt,
    get_category,
    get_categories,
    create_category,
    ListSabtAPIView,
    RetrieveSabtAPIView,
)

#SET UP URLs FOR APP

urlpatterns = [
    path("sabts/create/", create_sabt, name="api_sabt_create"),
    path("sabts", ListSabtAPIView.as_view(), name="api_sabts_list"),
    path("sabts/<int:pk>", RetrieveSabtAPIView.as_view(), name="api_sabts_retrieve"),
    path("categories", get_categories, name="api_categories_list"),
    path("categories/<int:pk>", get_category, name="api_category_retrieve"),
    path("categories/create", create_category, name="api_category_create"),
]
