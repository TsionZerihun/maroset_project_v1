from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'job_status', 'admin_comment')
        
class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user' , 'job_status', 'admin_comment')

class JobAdminResponseForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_status', 'admin_comment']
