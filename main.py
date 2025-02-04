# num1 = int(input("Input the first digit: "))
# num2 = int(input("Input the second digit: "))


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

name = input()
price = int(input())
weight = int(input())
itogo = weight * price
money = int(input())
change = money - itogo
print(f'{"Чек":=^35}\nТовар:{name:>29}\nЦена:{price:>30}\nИтого:{itogo:>29}\nВнесено:{money:>27}\nСдача:{change:>29}')


