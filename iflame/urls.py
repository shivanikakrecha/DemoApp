from django.urls import path, include
from iflame.views import (
    Welcome, StudentList, StudentDetail, CourseCreateView, StudentInformationView,
    StudentEditView, StudentDeleteView, StudentListClassBasedView, StudentDetailView,
    StudentCreateView, StudentUpdateView, StudentInformationDeleteView, WelcomeView
)

app_name = 'iflame'

urlpatterns = [
    path('', StudentListClassBasedView.as_view()),

    path('student/<int:student_id>/', StudentDetailView.as_view(), name="student_detail"),
    path('course/create', CourseCreateView, name='course_create'),
    path('student/create', StudentCreateView.as_view(), name='student_create'),
    path('student/edit/<int:student_id>', StudentUpdateView.as_view(), name='student_edit'),
    path('student/delete/<int:student_id>',
         StudentInformationDeleteView.as_view(), name='student_delete')
]
