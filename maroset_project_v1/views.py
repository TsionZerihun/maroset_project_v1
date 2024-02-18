from django.shortcuts import render, redirect
from job.models import Job, ApplyJob,Industry
from company.models import Company
from .filter import Jobfilter
from django.core.paginator import Paginator
from job.form import ApplyJobsForm

def index(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(job_status='Approved').order_by('-timestamp'))
    p = Paginator(filter.qs,2)
    page = request.GET.get('page')
    filter_paginate = p.get_page(page)

    softwaredeveloper = Job.objects.filter(industry=1).count()
    graphicsdesign = Job.objects.filter(industry=2).count()
    socialmediamanagement = Job.objects.filter(industry=3).count()
    projectmanagement = Job.objects.filter(industry=4).count()
    enginering = Job.objects.filter(industry=5).count()
    Sales = Job.objects.filter(industry=6).count()
    teachingtranslation = Job.objects.filter(industry=7).count()
    others = Job.objects.filter(industry=8).count() 

    context = {'filter':filter,'softwaredeveloper':softwaredeveloper, 
    'graphicsdesign':graphicsdesign, 
    'socialmediamanagement':socialmediamanagement,
    'projectmanagement':projectmanagement,
    'enginering':enginering,
    'Sales' :Sales, 
    'teachingtranslation' :teachingtranslation,   
    'others':others,
    'filter_paginate':filter_paginate}
    return render(request, 'index/main.html', context)

def about(request):
    return render(request, 'index/about.html')

def contact(request):
    return render(request, 'index/contact.html')

def terms(request):
    return render(request, 'index/terms.html')

def job_list(request):
    the_jobs = Job.objects.filter(job_status='Approved').order_by('-timestamp')
    p = Paginator(the_jobs,2)
    page = request.GET.get('page')
    jobs= p.get_page(page)
    context = {'jobs': jobs}
    return render(request, 'index/job-list.html', context)

def job_detail(request,pk):
    user = request.user
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApplyJobsForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job=job
            var.user=user

          
            var.save()
        return redirect ('dashboard') 
    else:
        form = ApplyJobsForm()
        context = {'job': job, 'has_applied': has_applied, 'form':form}
        return render(request, 'index/job-detail.html', context)