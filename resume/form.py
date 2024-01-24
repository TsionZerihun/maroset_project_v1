from django import forms
from .models import Resume

class UpdateResumeForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['upload_resume'].required = True
    class Meta:
        model = Resume
        exclude = ('user' ,)
