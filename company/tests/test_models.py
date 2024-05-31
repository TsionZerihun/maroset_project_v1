from django.test import TestCase
from .models import Company, Startup

class Company(TestCase):
    def setUp(self):
        self.model_instance = Company.objects.create(field1='value1', field2='value2')

    def test_model_creation(self):
        self.assertTrue(isinstance(self.model_instance, Company))
        self.assertEqual(self.model_instance.__str__(), 'expected_string_representation')
