from django.urls import path
from .views import UserLoginView, UserLogoutView, UserPasswordChangeView, UserRegistrationView, profile, update_profile, RegisterDoneView, user_activate


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/', profile, name='profile'),
    path('edit/', update_profile, name='update_profile'),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('register/done', RegisterDoneView.as_view(), name='register_done'),
    path('register/activate/<str:sign>/', user_activate, name='register_activate')
]
