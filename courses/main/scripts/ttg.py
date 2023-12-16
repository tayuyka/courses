from main.models import Teacher, Group, Course
import random
#
# fio_list = [
#     "Дмитриев Максим Владимирович",
#     "Коркина Алла Романовна",
#     "Козлова Анна Александровна",
#     "Смирнов Алексей Игоревич",
#     "Кузнецова Елена Владимировна",
#     "Морозов Михаил Андреевич",
#     "Новикова Ольга Николаевна",
#     "Васнецов Артем Викторович",
#     "Павлова Екатерина Сергеевна",
#     "Медведев Игорь Александрович",
#     "Соколов Станислав Петрович",
#     "Зайцева Анастасия Дмитриевна",
#     "Киселев Кирилл Игоревич",
#     "Лебедева Наталья Алексеевна",
#     "Андреев Андрей Андреевич",
#     "Жукова Ирина Владимировна",
#     "Белов Борис Валентинович",
#     "Тарасова Татьяна Васильевна"
# ]
#
# courses_list = [
#     "Живопись", "Русский язык", "Английский язык",
#     "Java", "Электродинамика", "Механика", "Алгебра", "Геометрия"
# ]
#
#
# for c in courses_list:
#     for _ in range(2):
#         course = Course.objects.get(course_name=c)
#         experience = random.randint(5, 35)
#         Teacher.objects.create(full_name=fio_list.pop(), experience=experience, course=course)

teachers = list(Teacher.objects.all())
rep = []

groups = list(Group.objects.all())
for group in groups:
    eligible_teachers = [teacher for teacher in teachers if teacher.course == group.course]
    for teacher in eligible_teachers:
        if rep.count(teacher) < 3:
            group.teacher = teacher
            group.save()
            rep.append(teacher)
        else:
            continue

print('glhf')
