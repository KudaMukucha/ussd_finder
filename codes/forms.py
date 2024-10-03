from django import forms
from .models import Code

class CreateCodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['name','slug','code','description','category','is_active']

class UpdateCodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['name','slug','code','description','category','is_active']