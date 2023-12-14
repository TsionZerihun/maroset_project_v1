from django import forms
from .models import Company

class UpdateCompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user' ,)
