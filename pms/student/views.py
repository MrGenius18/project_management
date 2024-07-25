from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ManagerSignUpForm


# Create your views here.

class ManagerSignUpView(CreateView):
    model = User
    form_class =ManagerSignUpForm
    template_name = 'student/signup_form.html'
    #success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        kwargs['user_type'] = 'manager'
    
    def form_valid(self, form):
        user = form.save()
        #get email if form valid
        email=form.cleaned_data.get('email')
        print (email)
        #if res>0:
        #res = sendMail(email)
        #login(self.request, user)
        return redirect('/student/list/')
    
class MangerListView(ListView):
    model = User
    template_name = 'student/maillist.html'
    context_object_name = 'maillist'

def sendMail(request):
    subject = "welcome to django"
    message = "hello django"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mr.genius0180@gmail.com','pusadadiya1308@gmail.com']
    res = send_mail(subject,message,email_from,recipient_list)
    if res>0:
        print("mail sent")
    else:
        print("mail not sent")    
    print(res)
    return HttpResponse("mail sent")