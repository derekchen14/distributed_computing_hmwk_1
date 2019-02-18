from django.urls import path
from djangoApp import views
from rest_framework import routers

"""
# First Method
router = routers.DefaultRouter(trailing_slash=False)
router = routers.SimpleRouter()
router.register(r'students', views.StudentInfoViewSet)
router.register(r'courses', views.CourseViewSet)

urlpatterns = router.urls
"""

urlpatterns = [
    # path('$/', views.StudentInfo, name='studentInfo'),
    # path('', views.index, name='index'),
    # path('post/', views.individual_post, name='individual_post'),
    # path('djangoApp/',views.StudentInfoViewSet.as_view({'get': 'list', 'post':'retrieve'})),
    path('djangoApp/',views.StudentList.as_view() ),
    path('djangoApp/<int:pk>',views.StudentDetail.as_view() ),
]
