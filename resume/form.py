from django import forms
from .models import Resume

class UpdateResumeForms(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user' ,)
