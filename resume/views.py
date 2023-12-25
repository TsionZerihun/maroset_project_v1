from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from .form import UpdateResumeForms
from users.models import User

# update company
def update_resume(request):
    resume = Resume.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateResumeForms(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(pk=request.user.id)
            user.has_resume = True
            user.save()
            var.save()
            messages.info(request, 'Your resume sucessfully created!!')
            return redirect('update-resume')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('apply')
    else:
        form = UpdateResumeForms(instance=resume)
        context = {'form' : form}
        return render(request, 'resume/update_resume.html', context)
    
# view company details
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request, 'resume/resume_details.html', context)
