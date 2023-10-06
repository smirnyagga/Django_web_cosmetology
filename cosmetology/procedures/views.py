from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from cosmetology.settings import EMAIL_HOST_USER
from django.views.generic import ListView, DetailView

from django.core.cache import cache

from .forms import *
from .models import *


class ProceduresHome(ListView):
    model = Doctors
    template_name = 'procedures/start.html'
    context_object_name = 'doctors'


class CatList(ListView):
    model = Categories
    template_name = 'procedures/cat_list.html'
    context_object_name = 'categories'


class ProceduresCategory(ListView):
    model = Procedures
    template_name = 'procedures/procedures_of_category.html'
    context_object_name = 'proc'
    allow_empty = False

    def get_queryset(self):
        return Procedures.objects.filter(relation__category__slug=self.kwargs['cat_slug'])


class AllProcedures(ListView):
    paginate_by = 3
    model = Procedures
    template_name = 'procedures/all_proc.html'
    context_object_name = 'proc'
    allow_empty = False


class ProceduresDetail(DetailView):
    model = Procedures
    template_name = 'procedures/procedure_detail.html'
    context_object_name = 'proc'
    slug_url_kwarg = 'proc_slug'


class ApplicationCreate(CreateView):
    model = Applications
    success_url = reverse_lazy('success_application')
    form_class = ApplicationForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} {data["phone"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
    send_mail(subject,
    content,
    EMAIL_HOST_USER,
    [EMAIL_HOST_USER])


def success_application(request):
    template_name = 'procedures/app_success.html'
    return render(request, template_name)


class QuestionCreate(CreateView, ListView):
    model = Questions
    success_url = reverse_lazy('success_question')
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        questions = Questions.objects.filter(is_published=True)
        paginator = Paginator(questions, 3)
        page_number = int(self.request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        return context


def success_question(request):
    template_name = 'procedures/question_success.html'
    return render(request, template_name)


class RegisterUser(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'procedures/register.html'
    form_class = RegisterUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'procedures/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Что-то пошло не так!')
