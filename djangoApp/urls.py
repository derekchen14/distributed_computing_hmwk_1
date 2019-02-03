from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'students', views.StudentInfoViewSet, basename='students')

urlpatterns = [
    #path('$/', views.StudentInfo, name='studentInfo'),
    path('', views.index, name='index'),
    path('post/', views.individual_post, name='individual_post'),
    #path('djangoApp/',views.StudentInfoViewSet.as_view({'get': 'list', 'post':'retrieve'})),
]
urlpatterns += router.urls
