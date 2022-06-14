from django.urls import path, include, re_path
from .views import ThreadListView, ThreadDetailView, add_image,  index_view, CreateThread, UpdatePostAPIView, UserView, UpdateUserView, add_like_view, PostListView

urlpatterns = [
    path('sections/<slug:sec_slug>', ThreadListView.as_view(), name='section_api' ),
    path('threads/<slug:thread_slug>', ThreadDetailView.as_view(), name='thread_api'),
    path('posts/<slug:thread_slug>', PostListView.as_view()),
    path('index/', index_view),
    path('thread/create/', CreateThread.as_view()),
    path('post/update/<int:pk>', UpdatePostAPIView.as_view()),
    path('post/<int:pk>/add_like', add_like_view),
    path('get_user/', UserView.as_view()),
    path('post/<int:pk>/add_image', add_image),
    path('update_user/<int:pk>', UpdateUserView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
