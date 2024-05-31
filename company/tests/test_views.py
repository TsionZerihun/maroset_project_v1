from django.test import TestCase
from django.urls import reverse
from .models import Company

class CompanyDetailsViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='Test Company',
            description='A company for testing',
            # Add other required fields here
        )
    
    def test_company_details_view_url_exists_at_proper_location(self):
        response = self.client.get(f'/company/{self.company.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_company_details_view_accessible_by_name(self):
        response = self.client.get(reverse('company_details', args=[self.company.pk]))
        self.assertEqual(response.status_code, 200)

    def test_company_details_view_uses_correct_template(self):
        response = self.client.get(reverse('company_details', args=[self.company.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company/company_detail.html')

    def test_company_details_view_context(self):
        response = self.client.get(reverse('company_details', args=[self.company.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('company', response.context)
        self.assertEqual(response.context['company'], self.company)
