from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Resume

User = get_user_model()

class ResumeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.resume = Resume.objects.create(
            user=self.user,
            first_name='John',
            sur_name='Doe',
            phone_number=1234567890,
            role='Developer',
            motivation='I am very motivated.',
            qualification='BSc Computer Science',
            university='Test University',
            university_start_date='2020-01-01',
            university_end_date='2023-01-01',
            university_description='Studied computer science.',
            experience_title='Software Engineer',
            experience_company='Test Company',
            experience_start='2023-02-01',
            experience_end='2024-02-01',
            experience_description='Worked on various projects.',
            upload_resume=None
        )

    def test_resume_creation(self):
        self.assertEqual(self.resume.user.username, 'testuser')
        self.assertEqual(self.resume.first_name, 'John')
        self.assertEqual(self.resume.sur_name, 'Doe')
        self.assertEqual(self.resume.phone_number, 1234567890)
        self.assertEqual(self.resume.role, 'Developer')
        self.assertEqual(self.resume.motivation, 'I am very motivated.')
        self.assertEqual(self.resume.qualification, 'BSc Computer Science')
        self.assertEqual(self.resume.university, 'Test University')
        self.assertEqual(self.resume.university_start_date.strftime('%Y-%m-%d'), '2020-01-01')
        self.assertEqual(self.resume.university_end_date.strftime('%Y-%m-%d'), '2023-01-01')
        self.assertEqual(self.resume.university_description, 'Studied computer science.')
        self.assertEqual(self.resume.experience_title, 'Software Engineer')
        self.assertEqual(self.resume.experience_company, 'Test Company')
        self.assertEqual(self.resume.experience_start.strftime('%Y-%m-%d'), '2023-02-01')
        self.assertEqual(self.resume.experience_end.strftime('%Y-%m-%d'), '2024-02-01')
        self.assertEqual(self.resume.experience_description, 'Worked on various projects.')
        self.assertIsNone(self.resume.upload_resume)

    def test_resume_update(self):
        self.resume.first_name = 'Jane'
        self.resume.save()
        updated_resume = Resume.objects.get(id=self.resume.id)
        self.assertEqual(updated_resume.first_name, 'Jane')

    def test_resume_str(self):
        self.assertEqual(str(self.resume), 'John Doe')
