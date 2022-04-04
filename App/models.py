from email.policy import default
from django.db import models
from django.forms import CharField

Gender = (("1","Male"),("2","Female"),("3","Prefer not to say"))

class Research_Internship(models.Model):
    institute_name = models.CharField(max_length=100,default="",blank=True)
    research_statement = models.TextField(max_length=700,default="",blank=True)
    start_date = models.DateField(default="",blank=True)
    end_date = models.DateField(default="",blank=True)
    domain = models.CharField(max_length=100,deafult="",blank=True)
    prof_name = models.CharField(max_length=150,default="",blank=True)
    stipend = models.CharField(max_length=50,default="",blank=True)
    location = models.CharField(max_length=100,default="",blank=True)
    applied_numbers = models.CharField(max_length=50,default="",blank=True)
    status = models.BooleanField(default="",blank=True)

class prof_details(models.Model):
    prof_institute = models.CharField(max_length=200,default="",blank=True)
    email = models.EmailField(default="",blank=True)
    expertise_area = models.CharField(max_length=100,default="",blank=True)
    active_internships = models.URLField()

class student_details(models.Model):
    student_name = models.CharField(max_length=200,default="",blank=True)
    age = models.IntegerField(max_length=5,default="",blank=True)
    gender = models.CharField(choices=Gender, default='1')
    student_institute = models,CharField(max_length=200,default="",blank=True)
    student_email = models.EmailField(default="",blank=True)
    mobile = models.IntegerField(max_length=10,default="",blank=True)
    institute_email = models.EmailField(default="",blank=True)