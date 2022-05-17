from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count

from main.utils import DataMixin
from main.models import Thread, Section, Post

# Create your views here.
def index(request):
    d = {}
    for sec in DataMixin.sections:
        d[sec] = Thread.objects.filter(section_id=sec.pk).filter(is_open=False).annotate(cnt=Count('posts')).order_by('-cnt')[:5]
    context = {
        'sections' : DataMixin.sections,
        'secthread' : d
    }
    return render(request, 'arch_index.html', context=context)


class ThreadListView(DataMixin, ListView):
    model = Thread
    template_name = 'arch_by_section.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['thread_list'] = Thread.objects.filter(section_id=self.kwargs.get('pk')).filter(is_open=False)
        context['section'] = Section.objects.get(pk=self.kwargs.get('pk'))
        return context
    
    
def thread_view(request, pk):
    posts = Post.objects.filter(tread_id=pk)
    thread = Thread.objects.get(pk=pk)
    context = {
        'sections' : DataMixin.sections,
        'posts' : posts,
        'thread' : thread
    }
    
    return render(request, 'arch_thread.html', context=context)