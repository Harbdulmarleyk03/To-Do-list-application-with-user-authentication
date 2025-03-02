from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Task 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)

    class Meta: 
        model = User    
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email 
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title', 'description', 'complete']
