from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    fees = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    faculty = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class StudentInformation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.first_name
