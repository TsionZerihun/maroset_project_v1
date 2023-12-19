from django.shortcuts import render, redirect
from job.models import Job

def dashbaord(request):
    return render(request, 'dashbaord/dashboard.html')

def apply(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'dashbaord/apply.html', context)

def applied(request):
    return render(request, 'dashbaord/applied.html')

def jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render(request, 'dashbaord/post-jobs.html', context)

def company(request):
    return render(request, 'dashbaord/company.html')