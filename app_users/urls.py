from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegistrationView, profile, update_profile


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit/', update_profile, name='update_profile')
]
