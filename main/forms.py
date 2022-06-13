from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from .models import BadWords


class PostForm(forms.ModelForm):
    post_text = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Post
        fields = ('post_text',)
    '''      
   def clean_text(self):
        val = self.cleaned_data['post_text']
        for value in val.split():
            for word in BadWords.objects.all():
                if value.lower() == word.word :
                    raise ValidationError('В сообщениях не допускается мат!')
        return val
        '''
                
    
class CreateThread(forms.Form):
    thread_name = forms.CharField(max_length=100,  label='Название темы')
    post_text = forms.CharField(label='Введите сообщение', 
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    
    class Meta:
        fields = ('thread_name', 'post_text')
        
        
class SearchForm(forms.Form):
    text = forms.CharField(max_length=30, label='Поиск')
    
    class Meta:
        fields = ('text')