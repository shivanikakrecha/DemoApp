from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from iflame.models import StudentInformation
from iflame.forms import CourseForm, StudentInformationForm, ContactForm, SignUpForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView,
    FormView, View
)
from django.contrib.auth.models import User
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
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
        return redirect('/iflame')

    context['form'] = form
    return render(request, "iflame/student_edit.html", context)


def StudentDeleteView(request, student_id):
    student_object = StudentInformation.objects.get(id=student_id)

    if request.method == "POST":
        student_object.delete()
        return redirect('/iflame')

    return render(request, 'iflame/student_delete.html', {})


# @method_decorator(login_required, name='student_list')
class StudentListClassBasedView(LoginRequiredMixin, ListView):
    model = StudentInformation
    paginate_by = 20
    template_name = 'iflame/student_list.html'
    context_object_name = 'students'
    login_url = '/'

    def get_queryset(self):
        queryset = StudentInformation.objects.all()
        return queryset

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
    success_url = '/iflame'


class StudentUpdateView(UpdateView):
    model = StudentInformation
    form_class = StudentInformationForm
    template_name = 'iflame/student_edit.html'
    pk_url_kwarg = 'student_id'
    success_url = '/iflame'


class StudentInformationDeleteView(DeleteView):
    model = StudentInformation
    success_url = '/iflame'
    pk_url_kwarg = 'student_id'
    template_name = 'iflame/student_delete.html'


class WelcomeView(TemplateView):
    template_name = 'base.html'


class ContactView(FormView):
    template_name = 'iflame/contact.html'
    form_class = ContactForm
    success_url = '/iflame'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')

        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        user_obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, 'iflame/contact.html', {'form': form})


class SignUpView(CreateView):
    form_class = SignUpForm
    model = User
    success_url = '/iflame'
    template_name = 'registration/signup.html'

    # def form_valid(self, form):
    #     print('Form valid is calling')
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     print("invalid is calling")
    #     return render(self.request, 'registration/signup.html', {'form': form})


# def LogoutFunView(request):
#     logout(request)
#     return redirect("/")


class LogoutFunView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutFunView, self).get_redirect_url(*args, **kwargs)


class UserProfile(LoginRequiredMixin, ListView):

    context_object_name = 'userprofile'
    template_name = 'iflame/userprofile.html'
    login_url = '/'

    def get_queryset(self):
        qs = User.objects.filter(id=self.request.user.id)
        return qs


def change_password(request):
    context = {}
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('password_change')
    else:
        form = PasswordChangeForm(request.user)
    context['form'] = form
    return render(request, "registration/password_change_form.html", context)
