from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import create_quiz,quiz_questions


class UserForm(UserCreationForm):
    email=forms.EmailField(max_length=100,help_text='Required')

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Create_Quiz_Form(forms.ModelForm):
    class Meta:
        model=create_quiz
        fields=['title','password']
        widgets ={
            'password':forms.PasswordInput(),
        }

class Create_Quiz_Question(forms.ModelForm):
    class Meta:
        model=quiz_questions
        fields='__all__'