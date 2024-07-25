from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    class Meta():
        db_table = 'User'