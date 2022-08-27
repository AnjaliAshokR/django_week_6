from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy

class Accountform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        success_url = reverse_lazy('admin')