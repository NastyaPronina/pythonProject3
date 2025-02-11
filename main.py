# num1 = int(input("Input the first digit: "))
# num2 = int(input("Input the second digit: "))
from operator import truediv

# print("Result: ", num1 + num2)
# print("Result: ", num1 - num2)
# print("Result: ", num1 / num2)
# print("Result: ", num1 * num2)

# print("Я люблю: ", "\n1. Фильмы", "\n2. Minecraft", "\n3. Кока-кола")
# name = input("Как вас зовут?")
# print("Привет, ", name)
#
# string = input()
# print(f"{string}\n"*3)
#
# need = 38 * 2.5
# answer = has - need
# print(answer)

# product = input("Input product: ")
# price = int(input("Input price: "))
# weight = int(input("Input weight: "))
# money = int(input("Input money: "))
# cost = price * weight
# change = money - cost
# if cost > money:
#     print(f"Чек\n {product} - {weight}кг - {price}руб/кг\n Итого: {cost}руб\n Внесено: {money}руб\n Сдача: {0}руб")
# else:
#     print(f"Чек\n {product} - {weight}кг - {price}руб/кг\n Итого: {cost}руб\n Внесено: {money}руб\n Сдача: {change}руб")

# n = int(input())
# # print("Купи слона!\n"*n)
# print("Купи слона!\n" * n)

# n = int(input())
# punishment = input()
# print(f'Я больше никогда не буду писать "{punishment}"!\n' * n)

# n = int(input("Введите количество детей: "))
# m = int(input("Введите количество минут: "))
# answer = int(n * m * 0.5)
# print(answer)
#
# name = input("Введите имя: ")
# number_cupboard = int(input("Введите номер шкафчика: "))
# group_number = number_cupboard // 100
# baby_number = number_cupboard % 100 % 10
# bed_number = number_cupboard // 10 % 10
# print(f'Группа № {group_number}.\n{baby_number}. {name}.\nШкафчик: {number_cupboard}.\nКроватка: {bed_number}.')

# digit = int(input())
# d = digit % 10 # последняя цифра
# digit //= 10 # обрезали последнюю цифру для удобства
# w = digit % 10 # вторая цифра с конца
# digit //= 10 # обрезали предпоследнюю цифру
# n = digit % 10 # третяя цифра с конца
# m = digit // 10 # четвертая цифра
# print(d, w, n, m, sep="")

# num_1 = int(input())
# num_2 = int(input())
# a = num_1 % 100 % 10
# b = num_1 % 100 // 10
# c = num_1 // 100
# d = num_2 % 100 % 10
# e = num_2 % 100 // 10
# f = num_2 // 100
# print((c + f) % 10, (b + e) % 10, (a + d) % 10, sep="")

# n = int(input())
# m = int(input())
# answer = m // n
# ostatok = m % n
# print(f'{answer}\n{ostatok}')

# n_red = int(input())
# n_green = int(input())
# n_blue = int(input())
# print(n_red + n_blue + 1)

# n = int(input())
# m = int(input())
# t = int(input())
# interval_1 = n * 60 + m
# interval_2 = interval_1 + t
# print(f"{interval_2 // 60 % 24:02}:{interval_2 % 60:02}")

# a = int(input())
# b = int(input())
# c = int(input())
# # print(float(abs(a - b) / c))
# print(f'{(abs(a - b) / c):.2f}')

# whole_sum = int(input())
# sum = int(input(), 2)
# print(sum + whole_sum)
#
# price = int(input(), 2)
# nominal = int(input())
# print(nominal - price)

# name = input()
# price = int(input())
# weight = int(input())
# itogo = weight * price
# money = int(input())
# change = money - itogo
# print(f'{"Чек":=^35}\nТовар:{name:>29}\nЦена:{price:>30}\nИтого:{itogo:>29}\nВнесено:{money:>27}\nСдача:{change:>29}')

# n = int(input())
# m = int(input())
# k_1 = int(input())
# k_2 = int(input()) # k_2 > k_1
# x = n * (m - k_2) // (k_1 - k_2)
# y = n - (n * (m - k_2) // (k_1 - k_2))
# print(x, y)

# =============if-esle===============
# name = input()
# answer = input()
# print("Как Вас зовут?")
# print("Здравствуйте, ", name, "!", sep="")
# print("Как дела?")
# if answer=="хорошо":
#     print("Я за вас рада!")
# else:
#     print("Все наладится!")

# speed_Petya = int(input())
# speed_Vasya = int(input())
# distance = 43872
# time_Petya = distance // speed_Petya
# time_Vasya = distance // speed_Vasya
# if time_Petya > time_Vasya:
#     print("Вася")
# else:
#     print("Петя")

# distance = 43872
# speed_Petya = int(input())
# speed_Vasya = int(input())
# speed_Tolya = int(input())
# time_P = distance // speed_Petya
# time_V = distance // speed_Vasya
# time_T = distance // speed_Tolya
# if time_P < time_V and time_P < time_T:
#     print("Петя")
# elif time_V < time_P and time_V < time_T:
#     print("Вася")
# else:
#     print("Толя")

# distance = 43872
# speed_Petya = int(input())
# speed_Vasya = int(input())
# speed_Tolya = int(input())
# if max(speed_Petya, speed_Vasya, speed_Tolya) == speed_Petya:
#     if speed_Vasya > speed_Tolya:
#         print("1. Петя\n2. Вася\n3. Толя")
#     else:
#         print("1. Петя\n2. Толя\n3. Вася")
# elif max(speed_Petya, speed_Vasya, speed_Tolya) == speed_Vasya:
#     if speed_Petya > speed_Tolya:
#         print("1. Вася\n2. Петя\n3. Толя")
#     else:
#         print("1. Вася\n2. Толя\n3. Петя")
# else:
#     if speed_Petya > speed_Vasya:
#         print("1. Толя\n2. Петя\n3. Вася")
#     else:
#         print("1. Толя\n2. Вася\n3. Петя")

# k = [3, 4, 2, 1, 9]
# temp = 0
#
# for i in range(len(k)-1):
#     for j in range(len(k)-1):
#         if k[j] > k[j+1]:
#             temp = k[j+1]
#             k[j+1] = k[j]
#             k[j] = temp

# [3, 2, 1, 4, 9]
# [2, 1, 3, 4, 9]
# [1, 2, 3, 4, 9]
# [1, 2, 3, 4, 9]
# [1, 2, 3, 4, 9]
# print(k)

# k = [3, 4, 2, 1, 9]

# найти максимальный элемент массива
# max = -999
# for i in range(len(k)):
#     if k[i] > max:
#         max = k[i]
# print(max)

# найти сумму элементов массива
# sum = 0
# for i in range(len(k)):
#     sum = sum + k[i]
# print(sum)

# вывести массив в обратном порядке
# print(k[::-1])
# arr1 = [3, 4, 2, 1, 9]
# arr2 = [0] * 5
# for i in range(len(arr1), 0, -1):
#     print(i)
#     arr2[len(arr1)-i] = arr1[i-1]
#
# print(arr2)

# arr1 = [3, 4, 2, 1, 9]
# arr1.append(14)
# arr1.reverse()
# print(arr1)

# поменять местами максимальный и минимальный элемент массива
# arr1 = [1, 2, 5, 4]
# max = 0
# min = 999
# for i in range(len(arr1)):
#     if arr1[i] > max:
#         max = arr1[i]
#     if arr1[i] < min:
#         min = arr1[i]
# print(max, min)
#     temp = max
#     max = min
#     min = max
# print(arr1)

# k = [3, 4, 2, 1, 9]
# temp = 0
#
# for i in range(len(k)-1):
#     for j in range(len(k)-1):
#         if k[j] > k[j+1]:
#             temp = k[j+1]
#             k[j+1] = k[j]
#             k[j] = temp

# [3, 2, 1, 4, 9]
# [2, 1, 3, 4, 9]
# [1, 2, 3, 4, 9]
# [1, 2, 3, 4, 9]
# [1, 2, 3, 4, 9]
# print(k)


# """Сортировка пузырьком Напишите программу,
# которая запрашивает у пользователя список чисел и сортирует его методом пузырька.
# Программа должна выводить список после каждой итерации сортировки."""
# arr = [int(input()) for i in range(3)]
# temp = 0
#
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             temp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = temp
#             print(arr)
# print(f"отсортированный массив: {arr}")


# """Бинарный поиск Напишите программу, которая запрашивает у пользователя отсортированный
# список чисел и число для поиска. Программа должна использовать бинарный поиск для
# определения, содержится ли число в списке. Программа должна выводить индекс числа
# в списке или сообщение о том, что число не найдено.
# """
# arr = [2, 3, 5, 7, 8, 18, 20]
# item = int(input("Введите число: "))
# flag = False
# left = -1
# right = len(arr)
# while right > left + 1:
#     middle = (left + right) // 2
#     if arr[middle] > item:
#         right = middle
#     elif arr[middle] == item:
#         flag = True
#         print(middle)
#         break
#     else:
#         left = middle
#
# if not flag:
#     print("Число не найдено")

# Быстрая сортировка (Quick Sort) Напишите
# программу, которая запрашивает у пользователя список чисел и сортирует его с использованием
# алгоритма быстрой сортировки. Программа должна выводить отсортированный список после
# завершения сортировки.


# Вывести все натуральные числа до введенного с клавиатуры
# n = int(input())
# for num in range (2, n + 1):
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if num%i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, " ", end = '')


# voice = input()
# while voice != "Три!":
#     print("Режим ожидания...")
#     voice = input()
# print("Ёлочка, гори!")

# count = 0
# line = "березка елочка зайка волк березка зайка"
# if 'зайка' in line:
#     print('-')

# arr = [3, 11, 7, 11, 12, 18, 19]
# i = 3
# j = 2
#
# for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         print(f"Итерация {i}: {arr}")
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j = j - 1
#         arr[j + 1] = key
#         print(f"После вставки: {arr}")
# ===================================================== массивы ==============================================================
#
arr = [3, 2, 4, 2]
# d_1, d_2, d_3 = arr
# print(d_3)
# print(len(arr))
# print(sorted(arr))
# print(max(arr))
# arr.append(8) # добавляет элемент массива в конец списка
# arr.extend([1, 2, "b"]) # добавляет несколько значений в конец списка
# arr.insert(0, 7) # добавляет значение в начало списка (индекс, что вставить)
# arr.remove(2) # удаляет первое вхождение элемента 2
# arr.clear() # очищает весь массив
# print(arr.pop(3)) # удаляет и возвращает элемент с заданным индексом
# print(arr)
# arr.reverse()
# print(arr.count(2)) # выводит кол-во повторений элемента заданного
# arr_1 = arr.copy() # создает копию массива
# print(arr.index(4)) # возвращает индекс элементов
# print(arr)

"""
Список студентов
"""
# students = []
# students.append("Mike")
# students.append("John")
# students.append("Sara")
# students.remove("Sara")
# print(students.index("Mike"))
# print(students)

"""
Список чисел
"""
# digits = [1, 2, 5, 3, 4, 5]
# digits.reverse()
# digits.sort(reverse=True)
# print(digits.count(5))
# print(digits)

"""
Работа со списками и циклы
"""
# digits = [1, 4, 2, 6]
# digits_1 = []
# for i in digits:
#     digits_1.append(i*2)
# print(digits_1)

"""
match case:
"""
# value = int(input("Enter digit "))
# match value:
#     case 1:
#         print(f"Выбрано значение {value}")
#     case 2:
#         print(f"Выбрано значение {value}")
#     case 3:
#         print(f"Выбрано значение {value}")
#     case 4:
#         print(f"Выбрано значение {value}")

"""
Меню
"""
# students = ["Sara", "Pit", "John"]
# while True:
#     print("1. Добавление студента")
#     print("2. Отчисление студента")
#     print("3. Вывести список студентов")
#     print("4. Отсортировать список студентов")
#     print("5. Добавление студента")
#     choose = int(input("Введите значение "))
#     match choose:
#         case 1:
#             students.append("Mike")
#         case 2:
#             students.remove("Sara")
#         case 3:
#             print(students)
#         case 4:
#             print(students.sort())
#         case 5:
#             break
#         case _:
#             print("bye")

students = ["Sara", "Pit", "John", "Peter"]
new_students = []
for i in students:
    new_students.append(i[0])
# посчитать сколько раз встречается каждая заглавная буква, которую мы добавили в новый массив
for i in new_students:
    if new_students.count(i) > 1:
        new_students.remove(i)
print(new_students)

