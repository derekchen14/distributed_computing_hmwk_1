from rest_framework import serializers
from .models import StudentInfo, Course


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        #fields = ('STUDENT_ID', 'STUDENT_NAME', 'STUDENT_YEAR', 'REGISTERED_COURSES')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
