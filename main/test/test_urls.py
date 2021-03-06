from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from main.views import AllSabt, create_sabt, Sabt, CreateCategory, CategorySabts


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
        self.assertEqual(resolve(url).func, create_sabt)

    def test_Sabt_url_view(self):
        url = reverse("main:Sabt", kwargs={"pk": 5})
        self.assertEqual(resolve(url).func.view_class, Sabt)

    def test_CreateCat_url(self):
        response = self.client.get(reverse("main:CreateCategory"))
        self.assertEqual(response.status_code, 200)

    def test_CreateCat_url_view(self):
        url = reverse("main:CreateCategory")
        self.assertEqual(resolve(url).func.view_class, CreateCategory)

    def test_category_sabt_url_view(self):
        url = reverse("main:CategorySabts", kwargs={'slug': 't_cat'})
        self.assertEqual(resolve(url).func.view_class, CategorySabts)
