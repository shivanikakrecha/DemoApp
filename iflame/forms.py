from django import forms
from iflame.models import Course, StudentInformation


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'content', 'faculty']


class StudentInformationForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = StudentInformation
        fields = '__all__'


class ContactForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField()
