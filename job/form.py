from django import forms
from .models import Job,ReportedJob

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


class ReportJobForm(forms.ModelForm):
    class Meta:
        model = ReportedJob
        exclude = ('reported_by' , 'reported_job')
