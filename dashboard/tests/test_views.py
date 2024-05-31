from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from job.models import Job, ApplyJob, ReportedJob
from company.models import Company, Startup
from resume.models import Resume

class DashboardViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.job = Job.objects.create(
            title='Test Job',
            description='Test Description',
            job_status='Approved',
            user=self.user
        )

        self.apply_job = ApplyJob.objects.create(
            user=self.user,
            job=self.job
        )

        self.resume = Resume.objects.create(
            user=self.user,
            title='Test Resume'
        )

        self.company = Company.objects.create(
            name='Test Company',
            user=self.user
        )

        self.startup = Startup.objects.create(
            name='Test Startup',
            user=self.user
        )

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
        self.assertIn('resume', response.context)

    def test_apply_view(self):
        response = self.client.get(reverse('apply'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/apply.html')
        self.assertIn('jobs', response.context)

    def test_applied_view(self):
        response = self.client.get(reverse('applied'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/applied.html')
        self.assertIn('jobs', response.context)

    def test_jobs_view(self):
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/post-jobs.html')
        self.assertIn('jobs', response.context)

    def test_company_view(self):
        response = self.client.get(reverse('company'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/company.html')
        self.assertIn('companys', response.context)
        self.assertIn('startups', response.context)

    def test_admin_index_view(self):
        response = self.client.get(reverse('admin_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/review_jobs.html')
        self.assertIn('jobs', response.context)

    def test_admin_view_users_view(self):
        response = self.client.get(reverse('admin_view_users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/user.html')
        self.assertIn('users', response.context)

    def test_admin_reported_jobs_view(self):
        response = self.client.get(reverse('admin_reported_jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/reported_jobs.html')
        self.assertIn('reported_jobs', response.context)

    def test_admin_jobs_view(self):
        response = self.client.get(reverse('admin_jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/review_jobs.html')
        self.assertIn('jobs', response.context)

# Add more tests as necessary for the other views
