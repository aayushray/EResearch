from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from .models import Student, Professor, Internship, Chat, Research_Room

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_name', 'age', 'student_institute', 'student_email',
        'mobile', 'institute_email')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'message', 'sender', 'receiver')


class ResearchRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_Room
        fields = ('professor', 'thread_topic')



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('user', 'email', 'prof_institute', 'expertise_area','active_internships')


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ('professor', 'institute_name', 'research_statement', 
        'start_date', 'end_date', 'domain', 'stipend', 'location', 'stipend', 
        'status', 'location')

        