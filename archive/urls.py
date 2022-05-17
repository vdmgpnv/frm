from django.urls import path
from .views import index, ThreadListView, thread_view

urlpatterns = [
    path('', index, name='archive'),
    path('sections/<int:pk>', ThreadListView.as_view(), name='arch_section'),
    path('thread/<int:pk>', thread_view, name='arch_thread'),
    
]