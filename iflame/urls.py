from django.urls import path, include
from iflame.views import Welcome, StudentList, StudentDetail

app_name = 'iflame'

urlpatterns = [
    path('', StudentList),
    path('student/<int:student_id>/', StudentDetail, name="student_detail"),
]
