from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from procedures.views import *

urlpatterns = [
    path('', cache_page(60)(ProceduresHome.as_view()), name='home'),
    path('cats/', CatList.as_view(), name='cat_list'),
    path('cats/<slug:cat_slug>', ProceduresCategory.as_view(), name='procedures_of_category'),
    path('procedure/<slug:proc_slug>', ProceduresDetail.as_view(), name='procedure_detail'),

    path('question/', QuestionCreate.as_view(), name='question'),
    path('success_question/', success_question, name='success_question'),

    path('application/', ApplicationCreate.as_view(), name='application'),
    path('success_application/', success_application, name='success_application'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]