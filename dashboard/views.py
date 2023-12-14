from django.shortcuts import render, redirect

def dashbaord(request):
    return render(request, 'dashbaord/dashboard.html')

def apply(request):
    return render(request, 'dashbaord/apply.html')

def applied(request):
    return render(request, 'dashbaord/applied.html')

def jobs(request):
    return render(request, 'dashbaord/post-jobs.html')

def company(request):
    return render(request, 'dashbaord/company.html')