from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table = "courses"
    
    def __str__(self):
        return self.name

class Student(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta():
        db_table = "student"

    def __str__(self):
        return self.name

#  faculty subjects batch

genderChoice = (('male','Male'),('female','Female'))

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(choices=genderChoice,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Faculty'

    def __str__ (self):
        return self.name
    
class Subjects(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Subjects'

    def __str__ (self):
        return self.name

class Batch(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Batch'

    def __str__ (self):
        return self.name

class User(models.Model):
    pass