from django.test import TestCase
from django.contrib.auth import get_user_model
from job.models import Industry, Job, ApplyJob, ConversationMessageJob, ReportedJob
from company.models import Company, Startup

User = get_user_model()

class IndustryModelTest(TestCase):
    def test_string_representation(self):
        industry = Industry(name="IT")
        self.assertEqual(str(industry), industry.name)

class JobModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.company = Company.objects.create(name='Test Company', user=self.user)
        self.startup = Startup.objects.create(name='Test Startup', user=self.user)
        self.industry = Industry.objects.create(name='IT')
        self.job = Job.objects.create(
            user=self.user,
            company=self.company,
            startup=self.startup,
            the_title="Test Job",
            location="Test Location",
            salary=50000,
            requirnment="Test Requirements",
            idel_candidate="Test Ideal Candidate",
            industry=self.industry,
            job_status="Approved"
        )

    def test_job_creation(self):
        self.assertIsInstance(self.job, Job)
        self.assertEqual(self.job.__str__(), self.job.the_title)

class ApplyJobModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.job = Job.objects.create(
            user=self.user,
            the_title="Test Job"
        )
        self.apply_job = ApplyJob.objects.create(
            user=self.user,
            job=self.job,
            description="Test Description"
        )

    def test_apply_job_creation(self):
        self.assertIsInstance(self.apply_job, ApplyJob)
        self.assertEqual(self.apply_job.user, self.user)
        self.assertEqual(self.apply_job.job, self.job)

class ConversationMessageJobModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.job = Job.objects.create(
            user=self.user,
            the_title="Test Job"
        )
        self.message = ConversationMessageJob.objects.create(
            job=self.job,
            content="Test Content",
            created_by=self.user
        )

    def test_conversation_message_creation(self):
        self.assertIsInstance(self.message, ConversationMessageJob)
        self.assertEqual(self.message.job, self.job)
        self.assertEqual(self.message.content, "Test Content")
        self.assertEqual(self.message.created_by, self.user)

class ReportedJobModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.job = Job.objects.create(
            user=self.user,
            the_title="Test Job"
        )
        self.reported_job = ReportedJob.objects.create(
            reported_by=self.user,
            reported_job=self.job,
            description="Test Description"
        )

    def test_reported_job_creation(self):
        self.assertIsInstance(self.reported_job, ReportedJob)
        self.assertEqual(self.reported_job.reported_by, self.user)
        self.assertEqual(self.reported_job.reported_job, self.job)
        self.assertEqual(self.reported_job.description, "Test Description")
