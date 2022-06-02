from django.urls import path
from .views import create_thread, delete_post, index, ThreadListView, thread_view, update_post, search_view


urlpatterns = [
    path('', index, name='index'),
    path('sections/<int:pk>', ThreadListView.as_view(), name='section'),
    path('thread/<int:pk>', thread_view, name='thread'),
    path('create_thread/<int:pk>', create_thread, name='create_th'),
    path('delete/<int:pk>', delete_post, name='delete'),
    path('edit_post/<int:pk>', update_post, name='edit_post'),
    path('search/', search_view ,name='search')
    
]
