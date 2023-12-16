from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('statistics/', statistics, name='statistics'),
    path('add-student/', add_student, name='add_student'),
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('view-students/', view_students, name='view_students'),
    path('view-teachers/', view_teachers, name='view_teachers'),
    path('view-courses/', view_courses, name='view_courses'),
    path('course/<int:course_id>/', course_info, name='course_info'),
    path('teacher/<int:teacher_id>/', teacher_info, name='teacher_info'),
    path('student/<int:student_id>/', student_info, name='student_info'),
    path('edit-student/<int:student_id>/', edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit-teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('delete-teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('edit-student/<int:student_id>/', edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
]
