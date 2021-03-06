from app_users.models import AdvUser
from django.db.models import Count
from django.shortcuts import get_object_or_404
from main.models import Post, Section, Thread
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import (ImageSerializer, PostSerializer, PostSerializersForThreadDetail,
                          SectionSerializer, ThreadListSerializers,
                          ThreadSerializer, UpdatePostSerializer,
                          UserSerializer)


class ThreadListView(APIView):
    
    def get(self, request, sec_slug):
        section = get_object_or_404(Section, slug=sec_slug)
        threads = Thread.objects.filter(section_id__slug=sec_slug)
        sec_serializer = SectionSerializer(section).data
        serializer = ThreadListSerializers(threads, many=True).data
        return Response({'section': sec_serializer, 'threads': serializer})    


class ThreadDetailView(APIView):

    def get(self, request, thread_slug):
        thread = get_object_or_404(Thread, slug=thread_slug)
        posts = Post.objects.filter(tread_id__slug=thread_slug)
        serializer = PostSerializersForThreadDetail(posts, many=True)
        return Response({'thread': thread.thread_name, 'posts': serializer.data})
    
    
    @permission_classes([IsAuthenticated,])
    def post(self, request, thread_slug):
        thread = get_object_or_404(Thread, slug=thread_slug)
        user = request.user
        request.data.update({'user_id': user.pk, 'tread_id': thread.pk})
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class CreateThread(CreateAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated,]
    

class UpdatePostAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdatePostSerializer
    permission_classes = [IsOwnerOrReadOnly,]
          
    
class UserView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)     

class UpdateUserView(UpdateAPIView):
    queryset = AdvUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    

class PostListView(ListAPIView):
    serializer_class = PostSerializersForThreadDetail
    permission_classes = [IsAuthenticatedOrReadOnly,]
    
    def get_queryset(self):
        posts = Post.objects.filter(tread_id__slug = self.kwargs['thread_slug'])
        return posts
    
 
@api_view(['POST', ])
@permission_classes([IsAuthenticated,])   
def add_like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    is_liked = False
        
    for like in post.likes.all():
        if like == request.user:
            is_liked = True
            break
            
    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    serializer = PostSerializersForThreadDetail(post)      
    
    return Response(serializer.data)
    
    
@api_view(['GET', ])
def index_view(request):
    sections = Section.objects.all()
    data = {}
    for sec in sections:
        threads = Thread.objects.filter(section_id=sec.pk).filter(
            is_open=True).annotate(cnt=Count('posts')).order_by('-cnt')[:5]
        data.update({f'section{sec.section_name}': SectionSerializer(sec).data,
                     f'threads{sec.section_name}': ThreadListSerializers(threads, many=True).data})
    return Response(data)



@api_view(['POST',])
def add_image(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.data.update({'post_id' : pk})
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
            
    return Response(serializer.data)