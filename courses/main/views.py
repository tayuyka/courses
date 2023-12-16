from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, Count, F


def home(request):

    return render(request, 'main/home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'main/add_student.html', {'form': form})


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'main/add_teacher.html', {'form': form})


# def view_students(request):
#     students = Student.objects.all()
#     return render(request, 'main/view_students.html', {'students': students})
def view_students(request):
    all_students = Student.objects.all()

    # Получение параметра запроса для фильтрации по ФИО
    search_query = request.GET.get('q', '')

    # Фильтрация студентов по ФИО
    if search_query:
        all_students = all_students.filter(full_name__icontains=search_query)

    students_per_page = 25

    paginator = Paginator(all_students, students_per_page)

    page = request.GET.get('page')

    try:
        students_page = paginator.page(page)
    except PageNotAnInteger:
        students_page = paginator.page(1)
    except EmptyPage:
        students_page = paginator.page(paginator.num_pages)

    context = {
        'students': students_page,
        'search_query': search_query,  # передаем обратно в шаблон для отображения в поле поиска
    }
    return render(request, 'main/view_students.html', context)


def view_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/view_teachers.html', {'teachers': teachers})


def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'main/view_courses.html', {'courses': courses})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentEditForm(instance=student)

    return render(request, 'main/edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('view_students')

    return render(request, 'main/delete_student.html', {'student': student})


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('view_teachers')
    else:
        form = TeacherEditForm(instance=teacher)

    return render(request, 'main/edit_teacher.html', {'form': form, 'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return redirect('view_teachers')

    return render(request, 'main/delete_teacher.html', {'teacher': teacher})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    groups = student.group.all()

    context = {
        'student': student,
        'groups': groups,
    }
    return render(request, 'main/student_info.html', context)


def teacher_info(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    groups = teacher.group_set.all()

    context = {
        'teacher': teacher,
        'groups': groups,
    }

    return render(request, 'main/teacher_info.html', context)


def course_info(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    groups = course.group_set.all()
    teachers = course.teacher_set.all()

    context = {
        'course': course,
        'groups': groups,
        'teachers': teachers,
    }

    return render(request, 'main/course_info.html', context)


def statistics(request):
    most_profitable_course = Course.most_expensive_course()
    most_popular_course = Course.most_popular_course()
    most_expensive_teacher = Teacher.highest_paid_teacher()
    most_profitable_student = Student.highest_paying_student()
    profit = most_profitable_course.calculate_profit()
    total_students = most_popular_course.total_students()
    salary = most_expensive_teacher.calculate_salary()
    total_cost = most_profitable_student.calculate_total_cost()

    context = {
        'most_profitable_course': most_profitable_course,
        'most_popular_course': most_popular_course,
        'most_expensive_teacher': most_expensive_teacher,
        'most_profitable_student': most_profitable_student,
        'profit': profit,
        'total_students': total_students,
        'salary': salary,
        'total_cost': total_cost,
    }

    return render(request, 'main/statistics.html', context)



