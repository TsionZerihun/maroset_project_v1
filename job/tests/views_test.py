from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Job, ApplyJob, ReportedJob
from .forms import CreateJobForm, UpdateJobForm, ReportJobForm

class JobViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.job = Job.objects.create(title='Test Job', description='Test Description', user=self.user)

    def test_create_job_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('create_job'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/create_job.html')

    def test_create_job_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_job'), {
            'title': 'New Job',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Job.objects.count(), 2)

    def test_update_job_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('Update_job', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/update_job.html')

    def test_update_job_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('Update_job', args=[self.job.id]), {
            'title': 'Updated Job',
            'description': 'Updated Description'
        })
        self.assertEqual(response.status_code, 302)
        self.job.refresh_from_db()
        self.assertEqual(self.job.title, 'Updated Job')

    def test_apply_to_job_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('apply_to_job', args=[self.job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ApplyJob.objects.filter(user=self.user, job=self.job).exists())

    def test_all_applicant_view(self):
        self.client.login(username='testuser', password='12345')
        ApplyJob.objects.create(user=self.user, job=self.job)
        response = self.client.get(reverse('all_applicant', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/all_applicants.html')

    def test_report_job_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('report_job', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'job/report_job_form.html')

    def test_report_job_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('report_job', args=[self.job.id]), {
            'reason': 'Inappropriate content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ReportedJob.objects.filter(reported_job=self.job).exists())

    def test_report_job_reason_view(self):
        reported_job = ReportedJob.objects.create(reported_job=self.job, reported_by=self.user, reason='Inappropriate content')
        response = self.client.get(reverse('report_job_reason', args=[reported_job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/reported_job_description.html')

    def test_about_reported_job_view(self):
        reported_job = ReportedJob.objects.create(reported_job=self.job, reported_by=self.user, reason='Inappropriate content')
        response = self.client.get(reverse('about_reported_job', args=[reported_job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_pages/about_reported_job.html')
