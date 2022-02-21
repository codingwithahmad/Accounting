from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from main.views import AllSabt, CreateSabt


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_AllSabt_url(self):
        response = self.client.get(reverse("main:AllSabt"))
        self.assertEqual(response.status_code, 200)

    def test_AllSabt_url_view(self):
        all_sabt = reverse('main:AllSabt')
        self.assertEqual(resolve(all_sabt).func.view_class, AllSabt)

    def test_CreateSabt_url(self):
        response = self.client.get(reverse("main:CreateSabt"))
        self.assertEqual(response.status_code, 200)

    def test_CreateSabt_url_view(self):
        url = reverse("main:CreateSabt")
        self.assertEqual(resolve(url).func.view_class, CreateSabt)
