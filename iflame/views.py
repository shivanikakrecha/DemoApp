from django.shortcuts import render, redirect
from django.http import HttpResponse
from iflame.models import StudentInformation
from iflame.forms import CourseForm, StudentInformationForm
# Create your views here.


def Welcome(request):
    # return HttpResponse("Welcome to the Iflame")
    return render(request, "base.html", {})


def StudentList(request):
    student_list = StudentInformation.objects.all()  # slice
    # student_list = StudentInformation.objects.filter(course__name="Python")
    return render(request, "iflame/student_list.html", {"students": student_list})


def StudentDetail(request, student_id):
    student_object = StudentInformation.objects.get(id=student_id)
    return render(request, 'iflame/student_detail.html', {'student': student_object})


def CourseCreateView(request):
    context = {}
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form
    return render(request, "iflame/create_course.html", context)


def StudentInformationView(request):
    form = StudentInformationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "iflame/create_course.html", {'form': form})
