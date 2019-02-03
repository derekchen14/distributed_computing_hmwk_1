from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import StudentInfo
from .serializer import StudentInfoSerializer
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.decorators import action


class StudentInfoViewSet(viewsets.ViewSet):
    #serializer_class = StudentInfoSerializer
    #queryset = StudentInfo.objects.all()

    def list(self, request):
        print(request)
        queryset = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(queryset, many=True)
        return HttpResponse(serializer.data)
    
    def retrieve(self, request, pk=None):
        #queryset = StudentInfo.objects.get(pk=int(request.data['STUDENT_ID']))
        queryset = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(queryset, many=True)
        return HttpResponse(serializer.data)

    def create(self, request):
        query_set = StudentInfo(STUDENT_ID='{}'.join(request.data['STUDENT_ID']),
                STUDENT_NAME='{}'.join(request.data['STUDENT_NAME']),
                STUDENT_YEAR='{}'.join(request.data['STUDENT_YEAR']),
                REGISTERED_COURSES='{}'.join(request.data['REGISTERED_COURSES']))
        query_set.save()
        return HttpResponse("Testing")



# Create your views here.
def index(request):
    return HttpResponse('Hello, welcome to the index page.')

def individual_post(request):
    student_ih = StudentInfo.objects.all()
    ans = StudentInfoSerializer(student_ih)
    #ans = serialize('json', student_ih)
    return HttpResponse(JSONRenderer().render(ans.data))
