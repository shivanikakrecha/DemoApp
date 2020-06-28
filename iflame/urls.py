from django.urls import path, include
from iflame.views import Welcome, StudentList, StudentDetail, CourseCreateView, StudentInformationView

app_name = 'iflame'

urlpatterns = [
    path('', StudentList),
    path('student/<int:student_id>/', StudentDetail, name="student_detail"),
    path('course/create', CourseCreateView, name='course_create'),
    path('student/create', StudentInformationView, name='student_create')
]
