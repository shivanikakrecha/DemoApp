from django import forms
from iflame.models import Course, StudentInformation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import os


class CourseForm(forms.ModelForm):
    avtar = forms.ImageField(required=False, widget=forms.FileInput)
    # start_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['name', 'content', 'faculty', 'avtar']

    def save(self, commit=True):
        instance = super(CourseForm, self).save(commit=False)

        import pdb; pdb.set_trace()
        if self.cleaned_data.get('avtar'):
            try:
                os.unlink(instance.avtar.path)
            except OSError:
                pass
            instance.avtar = None
        if commit:
            instance.save()
        return instance


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


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = [
        'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        ]
