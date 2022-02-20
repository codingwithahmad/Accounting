from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_AllSabt_url(self):
        response = self.client.get(reverse("main:AllSabt"))
        self.assertEqual(response.status_code, 200)
