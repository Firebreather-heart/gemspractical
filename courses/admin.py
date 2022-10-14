from django.contrib import admin
from .models import Subject,Task
# Register your models here.

# class SubjectInline(admin.StackedInline):
#     model = Subject

class TaskInline(admin.TabularInline):
    model = Task 

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name','subject','deadline']