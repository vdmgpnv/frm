from dataclasses import fields
from app_users.models import AdvUser
from djoser.serializers import UserCreateSerializer
from main.models import Image, Post, Section, Thread, BadWords
from rest_framework import serializers


class SectionSerializer(serializers.ModelSerializer):
    section_link = serializers.URLField(source='get_absolute_url')

    class Meta:
        model = Section
        fields = ('section_name', 'section_link')


class PostSerializersForThreadDetail(serializers.ModelSerializer):
    tread_id = serializers.StringRelatedField()
    user_id = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    user_register_date = serializers.DateTimeField(
        format='%d.%m.%Y', source='user_id.date_joined')
    images = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'text', 'tread_id', 'user_id', 'created_at',
                  'updated_at', 'user_register_date', 'likes', 'images')

    def get_images(self, obj):
        img_dict = {}
        for img in obj.images.all():
            img_dict[img.id] = img.img.url
        return img_dict
    
    def get_likes(self, obj):
        return obj.likes.count()

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('post_id', 'img')


class ThreadListSerializers(serializers.ModelSerializer):
    section_name = serializers.StringRelatedField(
        source='section_id.section_name')
    count_posts = serializers.SerializerMethodField()
    thread_link = serializers.URLField(source='get_absolute_url')
    section_link = serializers.URLField(source='section_id.get_absolute_url')

    class Meta:
        model = Thread
        fields = ('section_link', 'thread_name', 'count_posts',
                  'thread_link', 'section_name')

    def get_count_posts(self, obj):
        return obj.posts.count()


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text',)

    def validate_text(self, value):
        for val in value.split():
            for word in BadWords.objects.all():
                if value.lower() == word.word :
                    raise serializers.ValidationError('?? ???????????????????? ???? ?????????????????????? ??????!')
        return val

class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = ('section_id', 'thread_name', 'get_absolute_url')


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%d.%m.%Y', read_only=True)

    class Meta:
        model = AdvUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'date_joined', 'info', 'avatar')


class UserCreationSerializer(UserCreateSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AdvUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'password', 'avatar', 'email', 'info')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id', 'tread_id', 'text')


    def validate_text(self, value):
        for val in value.split():
            for word in BadWords.objects.all():
                if value.lower() == word.word :
                    raise serializers.ValidationError('?? ???????????????????? ???? ?????????????????????? ??????!')
        return val