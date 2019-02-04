from django.urls import path
from djangoApp import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
# router = routers.SimpleRouter()
router.register(r'students', views.StudentInfoViewSet)
router.register(r'courses', views.CourseViewSet)

"""
urlpatterns = [
    #path('$/', views.StudentInfo, name='studentInfo'),
    path('', views.index, name='index'),
    path('post/', views.individual_post, name='individual_post'),
    #path('djangoApp/',views.StudentInfoViewSet.as_view({'get': 'list', 'post':'retrieve'})),
]
"""
urlpatterns = router.urls
