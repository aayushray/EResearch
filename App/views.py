from concurrent.futures import thread
from sys import api_version
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentProfileSerializer, UserSerializer, ResearchRoomSerializer, ProfessorSerializer, InternshipSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from .models import Professor, Research_Room, Student, Internship
from rest_framework.parsers import JSONParser 
from rest_framework import status


# Create your views here.

def home(request):
    pass

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(('GET', 'POST'))
@permission_classes([IsAuthenticated])
def student_profile(request):
    if request.method=="POST":
        student_name = request.POST.get('student_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        student_institute = request.POST.get('student_institute')
        student_email = request.POST.get('student_email')
        mobile = request.POST.get('mobile')
        institute_email = request.POST.get('institute_email')
        user = request.user

        Student.objects.create(student_name=student_name, age=age,
        gender=gender, student_institute=student_institute, 
        student_email=student_email,
        mobile=mobile, institute_email=institute_email, user=user)       
        response = {
            "success":"successful"
        }
        return JsonResponse(response, status=status.HTTP_201_CREATED)

    else:
        student = get_object_or_404(Student, user=request.user)
        serializer = StudentProfileSerializer(student)
        return Response(serializer.data)



@api_view(('GET', 'POST'))
@permission_classes([IsAuthenticated])
def professor_profile(request):
    if request.method=="POST":
        try:
            user = request.user
            prof_institute = request.POST.get('prof_institute')
            email = request.POST.get('email')
            expertise_area = request.POST.get('expertise_area')
            active_internships = request.POST.get('active_internships')
            Professor.objects.create(user=user, prof_institute=prof_institute,
            email=email,expertise_area=expertise_area,active_internships=active_internships)
            response = {
                "success":"successful"
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            response = {
                'error':'All required fields are not filled'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:
        professor = get_object_or_404(Professor, user=request.user)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)


@api_view(('GET', 'POST'))
@permission_classes([IsAuthenticated])
def new_room(request):
    if request.method=="POST":
        # try:
        prof_profile = Professor.objects.filter(user=request.user)
        prof = prof_profile[0]
        thread_topic = request.POST.get('thread_topic')
        Research_Room.objects.create(professor=prof, thread_topic=thread_topic)
        response = {
            "success":"successful"
        }
        return Response(response, status=status.HTTP_201_CREATED)
    
                # response = {
                #     'error':'All required fields are not filled'
                # }
                # return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        # except:
        #     thread_topic = request.POST.get('thread_topic')
        #     response = {
        #         "No professor account found": thread_topic
        #     }
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:
        room = get_object_or_404(Research_Room, professor=request.user)
        serializer = ResearchRoomSerializer(room)
        return Response(serializer.data)


# @api_view(('GET', 'POST'))
# @permission_classes([IsAuthenticated])
# def message(request):
#     if request.method=="POST":
#         message = request.POST.get('message')
#         user = request.user
#         Chat.objects.create(message=message, user=user)
#         response = {
#             "success":"successful"
#         }
#         return JsonResponse(response, status=status.HTTP_201_CREATED)

#     else:
#         chat = get_object_or_404(Chat, user=request.user)
#         serializer = ChatSerializer(chat)
#         return Response(serializer.data)


@api_view(('GET', 'POST'))
@permission_classes([IsAuthenticated])
def internship(request):
    if request.method=='POST':
        user = request.user
        try:
            prof = Professor.objects.get(user=user)
            institute_name = request.POST.get('institute_name')
            research_statement = request.POST.get('research_statement')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            domain = request.POST.get('domain')
            stipend = request.POST.get('stipend')
            location = request.POST.get('location')
            applied_numbers = request.POST.get('applied_numbers')

            Internship.objects.create(professor=prof, institute_name=institute_name,
            research_statement=research_statement, start_date=start_date,
            end_date=end_date, domain=domain, stipend=stipend, location=location,
            applied_numbers=applied_numbers)

            response = {
                "success":"successful"
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            response = {
                'error':'All required fields are not filled'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:
        internship = get_object_or_404(Internship, professor=request.user)
        serializer = InternshipSerializer(internship)
        return Response(serializer.data)