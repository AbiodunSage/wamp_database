from django import forms
from .models import SampleModel

class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel
        fields = ['name', 'description', 'age', 'email', 'height', 'weight', 'is_active', 'occupation']