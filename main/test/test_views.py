from django.test import TestCase, Client
from django.urls import reverse
from main.models import Sabt
from django.utils import timezone
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_sabt = reverse('main:AllSabt')
        self.create_sabt = reverse('main:CreateSabt')
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
        response = self.client.post('http://127.0.0.1:8000/create' ,{
            'title': 'fruit',
            'income':0,
            'spending':25000,
            'date': timezone.now()
        })


        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sabt.objects.last().title, 'fruit')


