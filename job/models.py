from django.db import models
from users.models import User
from company.models import Company

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    the_title = models.CharField(max_length=100, null=True, blank=True)    
    location = models.CharField(max_length=100, null=True, blank=True)
    salary = models.PositiveBigIntegerField(default=35000, null=True, blank=True)
    requirnment = models.TextField(null=True, blank=True)
    idel_candidate = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.the_title
    

class ApplyJob(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)