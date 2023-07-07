from django.contrib import admin
from .models import raj

# Register your models here.

class showraj(admin.ModelAdmin):
    List = ['name','email']

admin.site.register(raj,showraj)