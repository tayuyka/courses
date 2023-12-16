from django.contrib import admin
from .models import Course, Student, Group, Teacher, CourseType

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(CourseType)
