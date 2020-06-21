from django.contrib import admin
from .models import StudentInformation, Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']
    list_filter = ['faculty', 'name']


admin.site.register(Course, CourseAdmin)
admin.site.register(StudentInformation)
