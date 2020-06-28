from django import forms
from iflame.models import Course, StudentInformation


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'content', 'faculty']


class StudentInformationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = StudentInformation
        fields = '__all__'
