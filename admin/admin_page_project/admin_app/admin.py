

# Register your models here.
from django.contrib import admin
from .models import Student, Notice

admin.site.register(Student)
admin.site.register(Notice)