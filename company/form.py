from django import forms
from .models import Company,Startup

#company
class CreateCompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)

class UpdateCompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)

#startup
class CreateStartupForms(forms.ModelForm):
    class Meta:
        model = Startup
        exclude = ('user',)


class UpdateStartupForms(forms.ModelForm):
    class Meta:
        model = Startup
        exclude = ('user',)
        
