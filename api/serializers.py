from dataclasses import field
from rest_framework import serializers
from app_users.models import AdvUser
from main.models import Section, Thread, Post


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

    class Meta:
        model = Post
        fields = ('id','text', 'tread_id', 'user_id', 'created_at',
                  'updated_at', 'user_register_date')


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


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user_id', 'tread_id', 'text')


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text',)


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = ('section_id', 'thread_name', 'get_absolute_url')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')
        
        
'''class UserCreationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AdvUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'avatar', 'email')
        '''