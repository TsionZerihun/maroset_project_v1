from django import forms
from .models import Job,ReportedJob,ApplyJob

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'job_status', 'admin_comment','location')
        
class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user' , 'job_status', 'admin_comment','location')

class JobAdminResponseForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_status', 'admin_comment']


class ReportJobForm(forms.ModelForm):
    class Meta:
        model = ReportedJob
        exclude = ('reported_by' , 'reported_job')


class ApplyJobsForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = ['description']
