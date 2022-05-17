from tabnanny import verbose
from ckeditor.fields import RichTextField

from django.db import models

from app_users.models import AdvUser

class Section(models.Model):
    section_name = models.CharField(max_length=30, unique=True, verbose_name='Раздел')
    
    def __str__(self) -> str:
        return self.section_name
    
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    
class Thread(models.Model):
    thread_name = models.CharField(max_length=100, verbose_name='Тема')
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')
    is_open = models.BooleanField(verbose_name='Открыто ли обсуждение?', default=True)   
    
    def __str__(self) -> str:
        return self.thread_name
    
    
    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'
    
    
class Post(models.Model):
    tread_id = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE, related_name='posts', verbose_name='Тема')
    user_id = models.ForeignKey(AdvUser, null=False, on_delete=models.CASCADE, related_name='posts', verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    text = RichTextField(max_length=1000, verbose_name='Текст сообщения')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
    def show_post(self):
        return self.text[0:100] + '...'
        
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    
    def __str__(self) -> str:
        return self.text[:10] + '...'
    
    

    