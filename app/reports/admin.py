from django.contrib import admin

from .models import Category, Remark, Student, Teacher, YearClass

admin.site.register(Category)
admin.site.register(Remark)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(YearClass)
