from django.db import models


class CourseType(models.Model):
    course_type = models.CharField(max_length=255)
    difficulty_coefficient = models.IntegerField()

    def __str__(self):
        return self.course_type


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    def calculate_profit(self):
        profit = 0
        groups = self.group_set.all()
        for group in groups:
            count = group.student_set.count()
            profit += group.calculate_cost() * count
        return profit

    @staticmethod
    def most_popular_course():
        courses = Course.objects.all()
        max_students = 0
        most_popular_course = None
        for course in courses:
            total_students = sum(group.student_set.count() for group in course.group_set.all())
            if total_students > max_students:
                max_students = total_students
                most_popular_course = course
        return most_popular_course

    def total_students(self):
        return sum(group.student_set.count() for group in self.group_set.all())

    @staticmethod
    def most_expensive_course():
        courses = Course.objects.all()
        max_cost = 0
        most_expensive_course = None
        for course in courses:
            profit = course.calculate_profit()
            if profit > max_cost:
                max_cost = profit
                most_expensive_course = course
        return most_expensive_course


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    experience = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    def calculate_salary(self):
        salary = 0
        groups = self.group_set.all()
        for group in groups:
            salary += 0.4 * group.calculate_cost() * group.student_set.count()
        return int(salary)

    @staticmethod
    def highest_paid_teacher():
        teachers = Teacher.objects.all()
        max_salary = 0
        highest_paid_teacher = None
        for teacher in teachers:
            salary = teacher.calculate_salary()
            if salary > max_salary:
                max_salary = salary
                highest_paid_teacher = teacher
        return highest_paid_teacher


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.group_name

    def calculate_cost(self):
        return (50 + self.course.course_type.difficulty_coefficient * 10 +
                self.teacher.experience * 5) * self.course.duration


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    group = models.ManyToManyField('Group')

    def __str__(self):
        return self.full_name

    def calculate_total_cost(self):
        total_cost = 0
        for group in self.group.all():
            total_cost += group.calculate_cost()
        return total_cost

    @staticmethod
    def highest_paying_student():
        students = Student.objects.all()
        max_cost = 0
        highest_paying_student = None
        for student in students:
            total_cost = student.calculate_total_cost()
            if total_cost > max_cost:
                max_cost = total_cost
                highest_paying_student = student
        return highest_paying_student