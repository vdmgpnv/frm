from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    post_text = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Post
        fields = ('post_text',)    
    
class CreateThread(forms.Form):
    thread_name = forms.CharField(max_length=100,  label='Название темы')
    post_text = forms.CharField(label='Введите сообщение',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    
    class Meta:
        fields = ('thread_name', 'post_text')
        
