from django.shortcuts import render, redirect
from job.models import Job, ApplyJob, ConversationMessageJob
from django.contrib import messages
from job.form import JobAdminResponseForm, CreateJobForm, UpdateJobForm
from users.models import User,ConversationMessageUser,Notification
from django.contrib.auth.decorators import login_required
from job.views import all_applicant
from users.utilities import create_notification
from company.models import Company, Startup

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
    jobs = Job.objects.filter(user=request.user)
    context = {'jobs': jobs}
    return render(request, 'dashbaord/post-jobs.html', context)

def company(request):
    companys = Company.objects.filter(user=request.user)
    startups = Startup.objects.filter(user=request.user)
    context = {'companys':companys, 'startups': startups}
    return render(request, 'dashbaord/company.html', context)

def admin_index(request):
    jobs = Job.objects.filter()
    context = {'jobs': jobs}
    return render(request, 'admin_pages/review_jobs.html', context)

def admin_view_users(request):
    users = User.objects.filter()
    context = {'users': users}

    return render(request, 'admin_pages/user.html',context)


def admin_reported_jobs(request):
    return render(request, 'admin_pages/reported_jobs.html')

def admin_jobs(request):
    jobs = Job.objects.filter()
    context = {'jobs': jobs}
    return render(request, 'admin_pages/review_jobs.html', context)


def admin_response(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        create_notification(request, job.user, 'application' ,jobname=job.the_title)

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
    if user.is_active:
        user.is_active = False
        user.save()
        return redirect('admin_users')
    else:
        messages.warning(request, f'user is already inactive')
        return redirect('admin_users')
def unblock_users(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        return redirect('admin_users')
    else:
        user.is_active = True
        user.save()
        return redirect('admin_users')


def message_job(request, pk):
    job = Job.objects.get(pk=pk)
    messages = ConversationMessageJob.objects.filter(job=pk)
    admin = User.objects.get(is_superuser=True)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessagejob = ConversationMessageJob.objects.create(job=job, content=content, created_by=request.user )
            return redirect('job-messages',pk=pk)
    

    context = {'job':job,'messages':messages,'admin':admin}
    return render(request, 'admin_pages/job_messages.html', context)
  
def user_message_job(request, pk):
    job = Job.objects.get(pk=pk)
    messages = ConversationMessageJob.objects.filter(job=pk)
    user = User.objects.get(pk=request.user.id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessagejob = ConversationMessageJob.objects.create(job=job, content=content, created_by=request.user )
            return redirect('job-owner-messages',pk=pk)
    
    else:
        context = {'job':job,'messages':messages,'user':user}
        return render(request, 'dashbaord/job_owner_messages.html', context)




def admin_chat_users(request):
    users = User.objects.filter()
    messages = ConversationMessageUser.objects.filter()

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessagejob = ConversationMessageUser.objects.create(user=request.user, content=content, created_by=request.user )
            return redirect('user-to-admin-chat')
    else:

        context = {'messages':messages,'users':users}

        return render(request, 'admin_pages/admin_to_user_chat.html', context)


def admin_with_one_user_chat(request, pk):
    user_contacted = User.objects.get(pk=pk)
    messages = ConversationMessageUser.objects.filter(user=pk)
    admin = User.objects.get(is_superuser=True)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessageuser = ConversationMessageUser.objects.create(user=user_contacted, content=content, created_by=request.user )
            create_notification(request, user_contacted, 'message', extra_id=request.user.id)

            return redirect('chat_specific_user',pk=pk)
        
    else:
        context = {'user_contacted':user_contacted,'messages':messages,'admin':admin}
        return render(request, 'admin_pages/personal_chat_admin_user.html', context)



def user_with_admin_chat(request, pk):
    user = User.objects.get(pk=pk)
    messages = ConversationMessageUser.objects.filter(user=pk)
    users = User.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)


    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            conversationmessageuser = ConversationMessageUser.objects.create(user=user, content=content, created_by=user )
            #create_notification(request, request.user, 'message', extra_id=request.user.id)
            return redirect('user_with_admin_chat',pk=pk)
        else:
            messages.warning(request, 'something went wrong')
            return redirect('user_with_admin_chat')
        
        

    else:
        context = {'messages':messages,'user':user}
        return render(request, 'users/chat.html', context)



#notification
@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('user_with_admin_chat', application_id=notification.extra_id)
        elif notification.notification_type == Notification.APPLICATION:
            return redirect('user_message_job', application_id=notification.extra_id)
    
    return render(request, 'base.html')