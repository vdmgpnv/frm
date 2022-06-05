from rest_framework import serializers

from main.models import Section, Thread, Post


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('section_id', 'section_name')


class PostSerializers(serializers.ModelSerializer):
    tread_id = serializers.StringRelatedField()
    user_id = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y')
    user_register_date = serializers.DateTimeField(
        format='%d.%m.%Y', source='user_id.date_joined')

    class Meta:
        model = Post
        fields = '__all__'


class ThreadListSerializers(serializers.ModelSerializer):
    section_name = serializers.StringRelatedField(
        source='section_id.section_name')
    count_posts = serializers.SerializerMethodField()
    thread_link = serializers.URLField(source='get_absolute_url')
    section_id = serializers.URLField(source='section_id.get_absolute_url')

    class Meta:
        model = Thread
        fields = ('section_id', 'thread_name', 'count_posts',
                  'thread_link', 'section_name')

    def get_count_posts(self, obj):
        return obj.posts.count()
