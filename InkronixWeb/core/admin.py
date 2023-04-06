from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','date_time','name','email','phone','details','interest','calling']
