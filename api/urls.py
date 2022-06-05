from django.urls import path
from .views import ThreadListView, ThreadDetailView, thread_list

urlpatterns = [
    path('sections/<slug:sec_slug>', ThreadListView.as_view(), name='section_api' ),
    path('thread/<slug:thread_slug>', ThreadDetailView.as_view(), name='thread_api')
]
