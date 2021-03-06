from forum.settings import ALLOWED_HOSTS
from app_users.models import AdvUser
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse, reverse_lazy


class Section(models.Model):
    section_name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Раздел'
    )
    slug = models.SlugField(
        max_length=255,
        auto_created=True,
        verbose_name='URL'
    )

    def __str__(self) -> str:
        return self.section_name

    def get_absolute_url(self):
        return reverse('section_api', kwargs={"sec_slug": self.slug})

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Thread(models.Model):
    thread_name = models.CharField(
        max_length=100,
        verbose_name='Тема'
    )
    section_id = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name='Раздел'
    )
    slug = models.SlugField(
        max_length=255,
        auto_created=True,
        verbose_name='URL'
    )
    is_open = models.BooleanField(
        verbose_name='Открыто ли обсуждение?',
        default=True
    )

    def __str__(self) -> str:
        return self.thread_name

    def get_absolute_url(self):
        return reverse_lazy('thread_api', kwargs={'thread_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.thread_name.replace(' ', '-')
        super(Thread, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'


class Post(models.Model):
    tread_id = models.ForeignKey(
        Thread,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Тема'
    )
    user_id = models.ForeignKey(
        AdvUser,
        null=False,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Опубликовано'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено'
    )
    text = RichTextField(
        max_length=1000,
        verbose_name='Текст сообщения'
    )
    likes = models.ManyToManyField(
        AdvUser,
        blank=True,
        related_name='likes'
    )

    def show_post(self):
        return self.text[0:100] + '...'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return self.text[:10] + '...'


class Image(models.Model):
    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='ID поста'
    )
    img = models.ImageField(
        upload_to='posts/',
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Картинка {self.pk} для новости: {self.post_id}'


class BadWords(models.Model):
    word = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = 'Плохое слово'
        verbose_name_plural = 'Плохие слова'
