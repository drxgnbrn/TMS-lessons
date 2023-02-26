# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person. Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# * Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# * Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).
# * Заверните код из пунктов 5 и 6 в функции get_oldest_pearson и filter_male_person соответственно.

from Person import Person

def get_oldest_person(friends):
    oldest = max(friends, key=lambda friend: friend.age)
    return oldest

def filter_male_person(friends):
    males = filter(lambda friend: friend.gender == 'M', friends)
    return list(males)

# create a list of friends
my_friends = [
    Person("Alice Smith", 28, "F"),
    Person("Bob Johnson", 35, "M"),
    Person("Charlie Brown", 30, "M"),
    Person("David Lee", 25, "M"),
    Person("Emily Davis", 27, "F")
]

# print info about each friend
for friend in my_friends:
    friend.print_person_info()

# print info about the oldest friend
oldest = get_oldest_person(my_friends)
print(f"The oldest person is:")
oldest.print_person_info()

# print info about male friends
males = filter_male_person(my_friends)
print(f"The male friends are:")
for male in males:
    male.print_person_info()