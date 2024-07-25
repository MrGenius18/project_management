from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = "/user/login/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'is_manager'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = 'Welcome to Project Management System'
        message = 'Thank you for registering with us'
        email_form = settings.EMAIL_HOST_USER
        send_mail(subject, message,email_form, recipient_list)
        login(self.request,user)
        return super().form_valid(form)

class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegisterForm
    template_name = 'user/developer_register.html'
    success_url = "/user/login/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'is_developer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        user = form.save()
        recipient_list = [email]
        subject = 'Welcome to Project Management System'
        message = 'Thank you for registering with us'
        email_form = settings.EMAIL_HOST_USER
        send_mail(subject, message,email_form, recipient_list)
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/cbv/filelist'
            else:
                return '/cbv/list/'

