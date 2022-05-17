from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


from main.utils import DataMixin

from .models import AdvUser
from .forms import AuthForm, RegistrationForm, UpdateProfileForm

# Create your views here.
class UserRegistrationView(DataMixin, CreateView):
    model = AdvUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['sections'] = self.sections
        return context
    
class UserLoginView(DataMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('profile')
    form = AuthForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = self.sections
        return context
    
class UserLogoutView(LogoutView):
    next_page = '/'
    
@login_required    
def profile(request):
    return render(request, 'profile.html', {'sections' : DataMixin.sections})


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            user = AdvUser.objects.get(pk=request.user.pk)
            user.info = form.cleaned_data['info']
            user.save()
            return redirect(reverse_lazy('profile'))
    else:
        form = UpdateProfileForm()
        context = {
            'form' : form,
            'sections' : DataMixin.sections
        }
        return render(request, 'update_profile.html', context=context)
            