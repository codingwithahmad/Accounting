from django.test import TestCase
from main.models import Sabt


class TestModels(TestCase):

    def setUp(self):
        self.sabt_milk = Sabt.objects.create(title="Milk Shake", income=0, spending=10000)

    def test_Sabt_str(self):
        self.assertEqual(self.sabt_milk.__str__(), "Milk Shake")
