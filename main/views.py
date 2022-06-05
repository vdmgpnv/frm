from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Count
from django.views.generic import ListView
from django.core.paginator import Paginator


from app_users.models import AdvUser
from .models import Section, Thread, Post
from .utils import DataMixin

from .forms import PostForm, CreateThread, SearchForm
from .models import Post, Section, Thread

# Create your views here.
def index(request):
    d = {}
    for sec in DataMixin.sections:
        d[sec] = Thread.objects.filter(section_id=sec.pk).filter(is_open=True).annotate(cnt=Count('posts')).order_by('-cnt')[:5]
    search_form = SearchForm()
    context = {
        'sections' : DataMixin.sections,
        'secthread' : d,
        'search_form' : search_form
    }
    return render(request, 'index.html', context=context)


class ThreadListView(DataMixin, ListView):
    model = Thread
    template_name = 'by_section.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['thread_list'] = Thread.objects.filter(section_id=self.kwargs.get('pk')).filter(is_open=True)
        context['section'] = Section.objects.get(pk=self.kwargs.get('pk'))
        context['sections'] = self.sections
        context['search_form'] = self.search_form
        return context
    
def thread_view(request, pk):
    posts = Post.objects.filter(tread_id=pk)
    thread = Thread.objects.get(pk=pk)
    post_form = PostForm
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'sections' : DataMixin.sections,
        'page_obj' : page_obj,
        'form' : post_form,
        'paginator' : paginator,
        'thread' : thread,
        'search_form' : DataMixin.search_form 
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
        'form' : create_thread,
        'search_form' : DataMixin.search_form 
    }
        return render(request, 'create_thread.html', context=context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    thread = Thread.objects.get(pk=post.tread_id.pk)
    post.delete()
    return redirect('thread', thread.pk)

def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.text = form.cleaned_data['post_text']
            post.updated_at = datetime.now()
            post.save()
            return redirect(f'/thread/{post.tread_id.pk}')
    else:
        form = PostForm(initial={'post_text' : post.text})
        context = {
            'sections' : DataMixin.sections,
            'form' : form,
            'search_form' : DataMixin.search_form 
        }
        return render(request, 'update_post.html', context)
        
            
def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        text = form.cleaned_data['text']
        threads = Thread.objects.filter(thread_name__icontains=text)
        return render(request, 'search_list.html', {'threads' : threads, 'search_form' : DataMixin.search_form, 
                                                    'sections' : DataMixin.sections})
    
    