from django.contrib import admin
from .models import *


class RelationInline(admin.TabularInline):
    model = Relation
    extra = 2


@admin.register(Procedures)
class ProceduresAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'photo', 'results', 'price', 'time', 'is_published']
    list_display_links = ['id', 'title', 'description']
    list_editable = ['price', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']
    inlines = [RelationInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'message']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'question', 'answer', 'is_published']
    list_editable = ['answer', 'is_published']
    list_filter = ['is_published']
    list_display_links = ['id', 'question']


