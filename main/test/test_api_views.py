import json
import datetime

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from main.models import Sabt, Category


class SabtTests(APITestCase):

    def setUp(self):
        self.cat1 = Category.objects.create(title='Books', slug='books')
        self.sabt1 = Sabt.objects.create(title="Litle Prince", income=0, spending=20000)
        self.sabt1.category.add(self.cat1)

    def test_get_all_sabts(self):
        """
        Ensure get request to /api/sabts get all sabts
        """

        url = reverse("main:api_sabts_list")
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
