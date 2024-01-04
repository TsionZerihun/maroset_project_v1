from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company,Startup
from .form import CreateCompanyForms,CreateStartupForms,UpdateCompanyForms,UpdateStartupForms
from users.models import User

#  company
def create_company(request):
    if request.method == 'POST':
        form = CreateCompanyForms(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user

            user = User.objects.get(id=request.user.id)

            user.has_company = True
            var.save()
            user.save()
            messages.info(request, 'account created sucessfully!!')
            return redirect('company')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('company')
    else:
        form = CreateCompanyForms()
        context = {'form' : form}
        return render(request, 'company/create_company.html', context)
    
# view company details
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    startup = Startup.objects.get(pk=pk)
    context = {'company': company,'startup': startup}
    return render(request, 'company/company_detail.html', context)

#startup

def startup_details(request, pk):
    company = Company.objects.get(pk=pk)
    startup = Startup.objects.get(pk=pk)
    context = {'company': company,'startup': startup}
    return render(request, 'company/startup_detail.html', context)
def create_startup(request):
    if request.method == 'POST':
        form = CreateStartupForms(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user

            user = User.objects.get(id=request.user.id)

            user.has_company = True
            var.save()
            user.save()
            messages.info(request, 'account created sucessfully!!')
            return redirect('company')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('company')
    else:
        form = CreateStartupForms()
        context = {'form' : form}
        return render(request, 'company/create_startup.html', context)
    


#update
def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompanyForms(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.info(request, 'job-update')
            return redirect('company')
        else:
            messages.warning(request, 'something went wrong')

            

    else:
        form = UpdateCompanyForms(instance=company)
        context = {'form' : form}
        return render(request, 'company/update_company.html', context)
    

# Update jobs
def update_startup(request, pk):
    startup = Startup.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateStartupForms(request.POST, instance=startup)
        if form.is_valid():
            form.save()
            messages.info(request, 'job-update')
            return redirect('company')
        else:
            messages.warning(request, 'something went wrong')

            

    else:
        form = UpdateStartupForms(instance=startup)
        context = {'form' : form}
        return render(request, 'company/update_startup.html', context)