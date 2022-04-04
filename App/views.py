from django.shortcuts import render
from django.http import HttpResponse
from models import Research_Internship,prof_details, student_details

# Create your views here.

def home(request):
    