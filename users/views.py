from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
from django.contrib.auth.decorators import login_required
from .models import Notification,ConversationMessageUser



# register applicants only
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
                var = form.save(commit=False)
                var.is_applicant = True
                var.is_recruiter = True
                var.username = var.email
                var.save()
                Resume.objects.create(user=var)
                messages.info(request, 'account created sucessfully!!')
                return redirect('login')
        else:
            messages.warning(request ,'password-rror')
            return redirect('register-applicant')
    else:
         form = RegisterUserForm()
         context = {'form': form}
         return render(request, 'users/register_applicant.html', context)
                

def blocked(request):
    return render(request,'users/account_block.html')


#login
def login_user(request):
     if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
          
        user = authenticate(request, username=email, password=password)
        if request.user.is_superuser:
            login(request, user)
            return redirect('administrator')
        
        
        elif user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        
        elif user is not request.user.is_active:
            return redirect('blocked')


        else:
             messages.warning(request, 'Wrong email or password')
             return redirect('login')
     else:
          return render(request, 'users/login.html')
     
#logout
def logout_user(request):
    logout(request)
    messages.info(request, 'your session has ended')
    return redirect('login')

          




            
               



    


     
     