from main.models import Course, Group
#
# # Список курсов
# courses_list = [
#     "Живопись", "Русский язык", "Английский язык",
#     "Java", "Электродинамика", "Python", "Механика", "Алгебра", "Геометрия"
# ]
#
# lol = [
#     "Жвпс", "Рус", "Англ",
#     "Java", "Элктрд", "Python", "Мех", "Алг", "Гмтр"
# ]
#
# # Список новых групп
# new_groups_list = ["3", "4", "5"]
#
# # Создаем новые группы для каждого курса
# for i in range(len(courses_list)):
#     course = Course.objects.get(course_name=courses_list[i])
#
#     for new_group_suffix in new_groups_list:
#         new_group_name = f"{lol[i]}-{new_group_suffix}"
#         Group.objects.create(group_name=new_group_name, course=course)
#
# print("Новые группы добавлены успешно.")

sorted_courses = Group.objects.all().order_by('group_name')

for group in sorted_courses:
    print(group.group_name)