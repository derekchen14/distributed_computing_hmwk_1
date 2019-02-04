from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    STUDENT_ID = models.IntegerField(primary_key=True, null=False)
    STUDENT_NAME = models.CharField(null=False, max_length=20)
    STUDENT_YEAR = models.CharField(null=False, max_length=20)
    REGISTERED_COURSES = models.CharField(max_length=500)
    objects = models.Manager()

class Course(models.Model):
    COURSE_ID = models.IntegerField(primary_key=True, null=False)
    COURSE_NAME = models.CharField(null=False, max_length=30)
    objects = models.Manager()
