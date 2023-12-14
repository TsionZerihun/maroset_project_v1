from django.shortcuts import render, redirect

def dashboard(request):
    return render(request, 'index/main.html')

def apply(request):
    return render(request, 'index/about.html')

def applied(request):
    return render(request, 'index/contact.html')

def jobs(request):
    return render(request, 'index/jobs.html')