from django.test import TestCase, Client
from django.urls import reverse
from main.models import Sabt, Category
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_sabt = reverse('main:AllSabt')
        self.create_sabt = reverse('main:CreateSabt')
        self.cat = Category.objects.create(title='t_cat', slug='t_cat')
        self.Sabt1 = Sabt.objects.create(
            title="sabt",
            income=10000,
            spending=0,
            date=timezone.now()
        )
        self.Sabt1.category.add(self.cat)

    def test_list_sabt_GET(self):
        response = self.client.get(self.list_sabt)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/all_sabt.html')

    def test_create_sabt_GET(self):
        response = self.client.get(self.create_sabt)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/create_sabt.html')

    def test_create_sabt_POST(self):
        category = Category.objects.create(title="fruit", slug="fruit")
        response = self.client.post(reverse('main:CreateSabt') ,{
            'title':'banana',
            'income':0,
            'spending':15000,
            'date': timezone.now(),
            'cats': category.pk
        })
        self.assertEqual(response.status_code, 200)
        self.assertEquals(Sabt.objects.last().title, 'banana')

    def test_detail_sabt_GET(self):
        """
        This function test main app and Sabt urls view
        """
        category = Category.objects.create(title="food", slug="food")
        sabt = Sabt.objects.create(pk=5, title='kobideh', income=0, spending=200000)
        sabt.category.add(category.pk)
        response = self.client.get(reverse('main:Sabt', kwargs={'pk': 5}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/sabt_details.html')

    def test_create_category_GET(self):
        """
        This function test get request to CreateCategory view
        """
        response = self.client.get(reverse('main:CreateCategory'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/create_cats.html')

    def test_create_category_POST(self):
        """
        This function test post request to CreateCategory view
        """

        response = self.client.post(reverse('main:CreateCategory'), {
            "title": "IT",
            "slug": "it"
        })


        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.last().title, 'IT')

    def test_category_sabt_GET(self):
        """
        This function test get request to CategorySabt view
        """

        response = self.client.get(reverse('main:CategorySabts', kwargs={'slug': 't_cat'}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/category_list.html')


