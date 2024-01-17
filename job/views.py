from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob,ReportedJob
from .form import CreateJobForm, UpdateJobForm,ReportJobForm
from users.models import User

# Create jobs
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            return redirect('jobs')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('jobs')

    else:
        form = CreateJobForm()
        context = {'form' : form}
        return render(request, 'job/create_job.html', context)


        
# Update jobs
def Update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'job-update')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong')

            

    else:
        form = UpdateJobForm(instance=job)
        context = {'form' : form}
        return render(request, 'job/update_job.html', context)
    
# Update jobs
def admin_Update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('administrator')
        else:
            messages.warning(request, 'something went wrong')

            

    else:
        form = UpdateJobForm(instance=job)
        context = {'form' : form}
        return render(request, 'job/admin_update_job.html', context)
    

def apply_to_job(request, pk):
    if request.user.is_authenticated:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission denied')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user = request.user
            )
            return redirect ('dashboard')   
    else:
        messages.info(request, 'Please login')
        return redirect('login')
    
def all_applicant(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job, 'applicants':applicants }
    return render(request, 'job/all_applicants.html', context)


def report_job(request, pk):
    reported_job = Job.objects.get(pk=pk)
    reported_by =  User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ReportJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.reported_by = reported_by
            var.reported_job = reported_job
            var.save()
            return redirect('jobs')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('report_job')
    else:
        form = ReportJobForm()
        if ReportedJob.objects.filter(reported_job=pk).exists():
            is_reported = True
        else:
            is_reported = False

        context = {'form' : form, 'is_reported': is_reported}
        return render(request, 'job/report_job_form.html', context)




def report_job_reason(request,pk):
    reported_job = ReportedJob.objects.filter(pk=pk)
    context = {'reported_job': reported_job}
    return render(request, 'admin_pages/reported_job_description.html',context)

def about_reported_job(request,pk):
    reported_job = ReportedJob.objects.filter(pk=pk)
    context = {'reported_job': reported_job}
    return render(request, 'admin_pages/about_reported_job.html',context)


