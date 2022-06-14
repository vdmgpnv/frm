
from .utilities import send_activation_notofocation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser



class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class RegistrationForm(UserCreationForm):
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        send_activation_notofocation(user)
        return user
    
    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')
        
        
class UpdateProfileForm(forms.ModelForm):
    info = forms.CharField(label='Расскажите о себе', required=False,
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'})) 
    class Meta:
        model = AdvUser
        fields = ('info', 'avatar')
        