import django.forms as form
from .models import *

class ManagerSignUpForm(form.ModelForm):
    class Meta:
        model = User
        fields = '__all__'