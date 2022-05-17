
from django.shortcuts import redirect, render
from django.db.models import Count
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from app_users.models import AdvUser
from .models import Section, Thread, Post
from .utils import DataMixin

from .forms import PostForm, CreateThread
from .models import Post, Section, Thread

# Create your views here.
def index(request):
    d = {}
    for sec in DataMixin.sections:
        d[sec] = Thread.objects.filter(section_id=sec.pk).annotate(cnt=Count('posts')).order_by('-cnt')[:5]
    context = {
        'sections' : DataMixin.sections,
        'secthread' : d
    }
    return render(request, 'index.html', context=context)


class ThreadListView(DataMixin, ListView):
    model = Thread
    template_name = 'by_section.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['thread_list'] = Thread.objects.filter(section_id=self.kwargs.get('pk')).filter(is_open=True)
        context['section'] = Section.objects.get(pk=self.kwargs.get('pk'))
        return context
    
def thread_view(request, pk):
    posts = Post.objects.filter(tread_id=pk)
    thread = Thread.objects.get(pk=pk)
    post_form = PostForm
    context = {
        'sections' : DataMixin.sections,
        'posts' : posts,
        'form' : post_form,
        'thread' : thread
    }
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            Post.objects.create(user_id=AdvUser.objects.get(pk=request.user.pk), tread_id=Thread.objects.get(pk=pk), text = post_form.cleaned_data['post_text'])
            return redirect(f'/thread/{pk}')
    else:
        return render(request, 'thread.html', context=context)
        
        
def create_thread(request, pk):
    if request.method == 'POST':
        create_thread = CreateThread(request.POST)
        if create_thread.is_valid():
            thread = Thread.objects.create(section_id = Section.objects.get(pk=pk), thread_name = create_thread.cleaned_data['thread_name'])
            Post.objects.create(user_id=request.user, tread_id=thread, text = create_thread.cleaned_data['post_text'])
            return redirect(f'/thread/{thread.pk}')
    else:
        create_thread = CreateThread()
        context = {
        'sections' : DataMixin.sections,
        'form' : create_thread
    }
        return render(request, 'create_thread.html', context=context)
