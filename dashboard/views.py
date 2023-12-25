from django.shortcuts import render, redirect
from job.models import Job, ApplyJob
from django.contrib import messages
from job.form import JobAdminResponseForm, CreateJobForm, UpdateJobForm
from users.models import User


def dashbaord(request):
    return render(request, 'dashbaord/dashboard.html')

def apply(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
   

    context = {'jobs': jobs}
    return render(request, 'dashbaord/apply.html', context)

def applied(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs': jobs}
    return render(request, 'dashbaord/applied.html', context)

def jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render(request, 'dashbaord/post-jobs.html', context)

def company(request):
    return render(request, 'dashbaord/company.html')

def admin_index(request):
    return render(request, 'admin_pages/main.html')

def admin_view_users(request):
    users = User.objects.filter()
    context = {'users': users}

    return render(request, 'admin_pages/user.html',context)


def admin_views_messages(request):
    return render(request, 'admin_pages/messages.html')

def admin_reported_jobs(request):
    return render(request, 'admin_pages/reported_jobs.html')

def admin_jobs(request):
    jobs = Job.objects.filter(job_status='Pending')
    context = {'jobs': jobs}
    return render(request, 'admin_pages/review_jobs.html', context)


def admin_response(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = JobAdminResponseForm(request.POST, instance=job)
        if form.is_valid():
            var = form.save()
            if var.job_status == 'Approve':
                messages.success(request, f'you have declined job post request for {job.user}')
                return redirect('admin_jobs')
            elif var.job_status == 'Decline':
                messages.success(request, f'you have declined job post request for {job.user}')
                return redirect('admin_jobs')
            else:
                return redirect('admin_jobs')

        else:
            messages.warning(request, f'somethign went wrong')
            return redirect('admin_jobs')
    else:
        form = JobAdminResponseForm(instance=job)
        context = {'form':form,'job':job}
        return render(request, 'admin_pages/admin_response.html', context)
            
                       
def block_users(request, pk):
    user = User.objects.get(pk=pk)
    if user is user.is_active:
        user.is_active = False
        return redirect('admin_users')
    else:
        messages.warning(request, f'user is already inactive')


