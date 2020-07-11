from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from iflame.models import StudentInformation
from iflame.forms import CourseForm, StudentInformationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
import datetime
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
    context['current_day'] = datetime.datetime.now()
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


def StudentEditView(request, student_id):
    context = {}
    student_object = StudentInformation.objects.get(id=student_id)
    form = StudentInformationForm(
        request.POST or None, instance=student_object)

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form
    return render(request, "iflame/student_edit.html", context)


def StudentDeleteView(request, student_id):
    student_object = StudentInformation.objects.get(id=student_id)

    if request.method == "POST":
        student_object.delete()
        return redirect('/')

    return render(request, 'iflame/student_delete.html', {})


class StudentListClassBasedView(ListView):
    model = StudentInformation
    paginate_by = 20
    template_name = 'iflame/student_list.html'
    context_object_name = 'students'

    # def get_queryset(self):
    #     queryset = StudentInformation.objects.filter(course__name='Python')
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['current_day'] = datetime.datetime.now().date()
    #     return context


class StudentDetailView(DetailView):
    model = StudentInformation
    context_object_name = 'student'
    template_name = 'iflame/student_detail.html'
    pk_url_kwarg = 'student_id'

    # def get_context_date(self, **kwargs):

    #     context = super().get_context_data(self, **kwargs)
    #     return context


class StudentCreateView(CreateView):
    model = StudentInformation
    # fields = ['student', 'course', 'is_paid']
    form_class = StudentInformationForm
    template_name = 'iflame/create_course.html'
    success_url = '/'


class StudentUpdateView(UpdateView):
        model = StudentInformation
        form_class = StudentInformationForm
        template_name = 'iflame/student_edit.html'
        pk_url_kwarg = 'student_id'
        success_url = '/'


class StudentInformationDeleteView(DeleteView):
    model = StudentInformation
    success_url = '/'
    pk_url_kwarg = 'student_id'
    template_name = 'iflame/student_delete.html'


class WelcomeView(TemplateView):
    template_name = 'base.html'