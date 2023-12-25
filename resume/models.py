from django.db import models
from users.models import User

# Create your resume model

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100, null=True, blank=True)
    sur_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)

    qualification = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    university_start_date = models.DateField(null=True, blank=True)
    university_end_date = models.DateField(max_length=1000,null=True, blank=True)
    university_description = models.TextField(null=True, blank=True)


    experience_title = models.CharField(max_length=100, null=True, blank=True)
    experience_company = models.CharField(max_length=100, null=True, blank=True)
    experience_start = models.DateField(null=True, blank=True)
    experience_end = models.DateField(null=True, blank=True)
    experience_description = models.TextField(max_length=1000,null=True, blank=True)

    upload_resume = models.FileField(upload_to='resume', null=True, blank=True)







    def __str__(self):
        return f'{self.first_name} {self.sur_name}'