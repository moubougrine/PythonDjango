from django import forms
from .models import Try

class Test(forms.ModelForm):
    class Meta:
        model = Try
        fields='__all__'

