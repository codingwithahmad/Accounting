from rest_framework import serializers
from .models import Sabt


class SabtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sabt
        fields = "__all__"
