# Задача 0. Дано число N. Найти все его делители. 
# Для каждого делителя укажите чётный он или нечётный

# def CheckEven(x):
#     if x % 2 == 0:
#         return ' - Четный'
#     else:
#         return ' - Нечетный'

# def Zadacha0():
#     number = int(input('Enter number: '))
#     for i in range(1, number+1):
#         if number % i == 0:
#             print(i, end = '')
#             print(CheckEven(i))

# Zadacha0()


# Задача1. Выведите таблицу истинности для выражения " не Х или У"

# x = [0, 1]
# y = [0, 1]

# print('x | y | ¬ X ∨ Y')
# for x in range(0, 2):
#     for y in range(0, 2):
#         sum = not x or y
#         print(f'{x} | {y} | {int(sum)}')     # Вывод числом
        # print(f'{x}, {y}, {bool(sum)}')      # Вывод (True, False)


# Задача2. Напишите программу, в которой
# пользователь будет задавать две строки, а программа
# - определять количество вхождений одной строки в другую. «qwe» «qwertyqwe» -> 2

# string_1 = input()
# string_2 = input()
# count = 0
# if len(string_1) > len(string_2):
#     for i in range(len(string_1)):
#         if string_2 == string_1[i:i+len(string_2)]:
#             count += 1
#     print('Количество совпадений строк:', count)
# else:
#     for i in range(len(string_2)):
#         if string_1 == string_2[i:i+len(string_1)]:
#             count += 1
#     print('Количество совпадений строк:', count)

# Второй вариант решения:

# symbols = 'qwe'
# phrase = 'qwertyqwe'
# count = 0
# lenSymbols = len(symbols)
# lenPhrase = len(phrase)
# r = range(0, lenPhrase - 2)
# for i in r:
#     if symbols == phrase[i:i+lenSymbols]:
#         count += 1
# print(count)

# Третий вариант через метод 'count' - строка 1 длиннее чем строка 2

# str1 = input('Введите текст1: ')
# str2 = input('Введите текст2: ')
# print(f'Текст1 включает в себя Текст2 {str1.count(str2)} time(s)')


# Задача3. Дано число N. Заполните список длиной N
# элементами 1, -3, 9, -27, 81, -243....  N = 5 -> [1, -3, 9, -27, 81]

# N = int(input('Введите число: '))
# list = []
# for i in range(0, N):
#     list.append((-3)**i)      # Добавить любое значение в список
# print(list)


# Задача 4. Найдите все числа до 10000, у которых
# количество делителей равно 10

# def check_number(n):

#     divigers = list()
#     for diviger in range(1, int(n ** 0.5)):
#         if n % diviger == 0:
#             divigers.append(diviger)
#     return len(divigers) == 5


# def find_numbers():
    
#     numbers = list()
#     for i in range(1, 10001):
#         if list(i) :
#             numbers.append(i)
#     return numbers

# print(*find_numbers())



