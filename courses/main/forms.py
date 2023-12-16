from django import forms
from django.core.validators import RegexValidator, MinValueValidator
from .models import Student, Teacher


class BasePersonForm(forms.ModelForm):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Zа-яА-Я\s]*$',
        message='Пожалуйста, введите только буквы.',

    )

    full_name = forms.CharField(
        label='ФИО',
        validators=[name_validator],
    )


class StudentForm(BasePersonForm):
    class Meta:
        model = Student
        fields = ['full_name', 'group']
        labels = {
            'full_name': 'ФИО',
            'group': 'Группа',
        }


class TeacherForm(BasePersonForm):
    non_negative_validator = MinValueValidator(
        limit_value=0,
        message='Опыт работы не может быть отрицательным.',
    )

    experience = forms.IntegerField(
        validators=[non_negative_validator],
        label='Опыт'
    )

    class Meta:
        model = Teacher
        fields = ['full_name', 'experience', 'course']
        labels = {
            'full_name': 'ФИО',
            'course': 'Курс',
        }


class StudentEditForm(BasePersonForm):
    class Meta:
        model = Student
        fields = ['full_name', 'group']
        labels = {
            'full_name': 'ФИО',
            'group': 'Группа',
        }


class TeacherEditForm(BasePersonForm):
    non_negative_validator = MinValueValidator(
        limit_value=0,
        message='Опыт работы не может быть отрицательным.',

    )

    experience = forms.IntegerField(
        validators=[non_negative_validator],
        label='Опыт'
    )

    class Meta:
        model = Teacher
        fields = ['full_name', 'experience', 'course']
        labels = {
            'full_name': 'ФИО',
            'course': 'Курс',
        }