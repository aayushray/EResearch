from email.policy import default
from django.db import models
from django.forms import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


Gender = (("Male","Male"),("Female","Female"),("Others","Others"))


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    prof_institute = models.CharField(max_length=200,default="",blank=True)
    email = models.EmailField(default="",blank=True)
    expertise_area = models.CharField(max_length=100,default="",blank=True)
    active_internships = models.URLField(blank=True, null=True)

class Internship(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    institute_name = models.CharField(max_length=100,default="",blank=True)
    research_statement = models.TextField(max_length=700,default="",blank=True)
    start_date = models.DateField(default="",blank=True)
    end_date = models.DateField(default="",blank=True)
    domain = models.CharField(max_length=100,default="",blank=True)
    stipend = models.CharField(max_length=50,default="",blank=True)
    location = models.CharField(max_length=100,default="",blank=True)
    status = models.BooleanField(default=True,blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    student_name = models.CharField(max_length=200,default="",blank=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=Gender, default='1', max_length=20)
    student_institute = models.CharField(max_length=200,default="",blank=True,null=True)
    student_email = models.EmailField(default="",blank=True,null=True)
    mobile = PhoneNumberField(blank=True,null=True)
    institute_email = models.EmailField(default="",blank=True,null=True)

class Research_Room(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    thread_topic = models.ForeignKey(Internship, on_delete=models.CASCADE)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Research_Room, on_delete=models.CASCADE)
    message = models.CharField(max_length=512, default="")