# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# * Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

from students import  Student


def calc_sum_scholarship(students):
    total_scholarship = 0
    for student in students:
        total_scholarship += student.get_scholarship()
    return total_scholarship

def get_excellent_student_count(students):
    count = 0
    for student in students:
        if student.is_excellent():
            count += 1
    return count

students = [
    Student("John Doe", 7.5),
    Student("Alice Smith", 8.9),
    Student("Bob Johnson", 6.0),
    Student("Emma Davis", 9.2),
    Student("Mike Wilson", 8.3)
]

total_scholarship = calc_sum_scholarship(students)
excellent_student_count = get_excellent_student_count(students)

print("Total scholarship amount: ", total_scholarship)
print("Number of excellent students: ", excellent_student_count)