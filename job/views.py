from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm

# Create jobs
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.info(request, 'New job has been create')
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
            messages.info(request, 'You Have Sucessfully applied')
            return redirect ('dashboard')   
    else:
        messages.info(request, 'Please login')
        return redirect('login')
    
def all_applicant(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job, 'applicants':applicants }
    return render(request, 'job/all_applicants.html', context)


