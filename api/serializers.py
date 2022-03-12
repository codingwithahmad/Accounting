from rest_framework import serializers
from main.models import Sabt, Category


class SabtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sabt
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
