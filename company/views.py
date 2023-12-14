from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .form import UpdateCompanyForms
from users.models import User

# update company
def update_company(request):
    company = Company.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCompanyForms(request.POST, instance=company)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            user.has_company = True
            var.save()
            user.save()
            messages.info(request, 'account created sucessfully!!')
            return redirect('jobs')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('login')
    else:
        form = UpdateCompanyForms(instance=company)
        context = {'form' : form}
        return render(request, 'company/update_company.html', context)
    
# view company details
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html', context)
