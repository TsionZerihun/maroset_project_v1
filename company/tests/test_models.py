from django.test import TestCase
from .models import YourModel

class YourModelTest(TestCase):
    def setUp(self):
        self.model_instance = YourModel.objects.create(field1='value1', field2='value2')

    def test_model_creation(self):
        self.assertTrue(isinstance(self.model_instance, YourModel))
        self.assertEqual(self.model_instance.__str__(), 'expected_string_representation')
