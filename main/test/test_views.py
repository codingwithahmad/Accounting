from django.test import TestCase, Client
from django.urls import reverse
from main.models import Sabt, Category
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_sabt = reverse('main:AllSabt')
        self.create_sabt = reverse('main:CreateSabt')
        self.detail_sabt = reverse('main:Sabt', kwargs={'pk': 5})
        self.Sabt1 = Sabt.objects.create(
            title="sabt",
            income=10000,
            spending=0,
            date=timezone.now()
        )

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

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sabt.objects.last().title, 'banana')

    def test_detail_sabt_GET(self):
        """
        This function is test main app and Sabt urls view
        """
        #Sabt.objects.create(pk=5, title='kobideh', income=0, spending=200000)
        response = self.client.get(self.detail_sabt)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/sabt_details.html')
