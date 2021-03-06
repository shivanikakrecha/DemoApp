from django.urls import path, include
from iflame.views import (
    Welcome, StudentList, StudentDetail, CourseCreateView, StudentInformationView,
    StudentEditView, StudentDeleteView, StudentListClassBasedView, StudentDetailView,
    StudentCreateView, StudentUpdateView, StudentInformationDeleteView, WelcomeView,
    ContactView, SearchView
)

app_name = 'iflame'

urlpatterns = [
    path('', StudentListClassBasedView.as_view(), name='student_list'),

    path('student/<int:student_id>/', StudentDetailView.as_view(), name="student_detail"),
    path('course/create', CourseCreateView, name='course_create'),
    path('student/create', StudentCreateView.as_view(), name='student_create'),
    path('student/edit/<int:student_id>', StudentUpdateView.as_view(), name='student_edit'),
    path('student/delete/<int:student_id>',
         StudentInformationDeleteView.as_view(), name='student_delete'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('search/', SearchView.as_view(), name='search_view')
]
