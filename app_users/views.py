from re import template
from django.core.signing import BadSignature
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required

from main.utils import DataMixin
from .utilities import signer
from .models import AdvUser
from .forms import AuthForm, RegistrationForm, UpdateProfileForm

# Create your views here.


class UserRegistrationView(DataMixin, CreateView):
    model = AdvUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('register_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    return render(request, 'profile.html', {'sections': DataMixin.sections})


def update_profile(request):
    user = AdvUser.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.info = form.cleaned_data['info']
            if form.cleaned_data['avatar'] is not None:
                user.avatar = form.cleaned_data['avatar']
            user.save()
            return redirect(to='profile')
    else:
        form = UpdateProfileForm(initial={'info': user.info})
        context = {
            'form': form,
            'sections': DataMixin.sections
        }
        return render(request, 'update_profile.html', context=context)


class UserPasswordChangeView(SuccessMessageMixin, 
                             LoginRequiredMixin, PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Пароль успешно изменен'
    
    
class RegisterDoneView(TemplateView):
    template_name = 'register_done.html'

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'sign/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_active:
        template = 'sign/user_is_activated.html'
    else:
        template = 'sign/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)