from django.shortcuts import render, redirect
from job.models import Job, ApplyJob
from company.models import Company



def dashboard(request):
    return render(request, 'index/main.html')

def job_list(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'index/job-list.html', context)

def job_detail(request,pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job': job, 'has_applied': has_applied}
    return render(request, 'index/job-detail.html', context)