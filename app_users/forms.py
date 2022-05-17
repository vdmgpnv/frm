
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'avatar')
        
class UpdateProfileForm(forms.Form):
    info = forms.CharField(label='Расскажите о себе',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = AdvUser
        fields = ('info',)