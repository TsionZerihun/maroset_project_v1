from django.db import models
from users.models import User
from company.models import Company,Startup

class Indusrty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    job_status_choices = (
        ('Approved', 'Approve'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    startup = models.ForeignKey(Startup, on_delete=models.DO_NOTHING, null=True, blank=True)
    the_title = models.CharField(max_length=100, null=True, blank=True)    
    location = models.CharField(max_length=100, null=True, blank=True)
    salary = models.PositiveBigIntegerField(default=35000, null=True, blank=True)
    requirnment = models.TextField(null=True, blank=True)
    idel_candidate = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Indusrty, on_delete=models.DO_NOTHING, null=True, blank=True)
    job_status = models.CharField(max_length=20, default='Pending', choices=job_status_choices, null=True, blank=True)
    admin_comment = models.TextField(null=True, blank=True)
    
    #def __str__(self):
    #    return self.the_title
    

class ApplyJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class ConversationMessageJob(models.Model):
    job = models.ForeignKey(Job, related_name='conversationmessagejob', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessagejob', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

