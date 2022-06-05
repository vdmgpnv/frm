from .serializers import PostSerializers, ThreadListSerializers
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Post, Section, Thread
from rest_framework.decorators import api_view

class ThreadListView(APIView):
    def get(self, request, sec_slug):
        threads = Thread.objects.filter(section_id__slug=sec_slug)
        serializer = ThreadListSerializers(threads, many=True)
        return Response(serializer.data) 


class ThreadDetailView(APIView):
    
    def get(self, request, thread_slug):
        posts = Post.objects.filter(tread_id__slug=thread_slug)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET',])
def thread_list(request, sec_slug):
    threads = Thread.objects.filter(section_id__slug=sec_slug)
    serializer = ThreadListSerializers(threads, many=True)
    return Response(serializer.data)