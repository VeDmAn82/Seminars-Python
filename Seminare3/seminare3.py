# Задача 0. Создайте скрипт func и функцию чтения
# последней строки файла. Вызовите её из скрипта example

# import example

# example.ReadLastRow()


# Задача 1. Дан файл, заполненный числами построчно.
# Считайте файл. Выведите все элементы, стоящие на
# чётных строках, а потом на нечётных

# def Numbers():
#     data = open('text1.txt', encoding='utf-8')
#     point = data.readlines()
#     data.close()
#     for i in range(0, len(point), 2):
#         print(point[i], end='')
#     print()
#     for i in range(1, len(point), 2):
#         print(point[i], end='')

# Number()


# Задача 2. При работе с документацией менеджер допустил
# ошибку, названия товаров перемешались с ценами. Помогите
# восстановить документ. Порядковый номер товара совпадает сномером цены   (без функции)

# data = open('text2.txt', encoding='utf-8')
# string = data.readline()
# data.close()
# clothes = []
# prices = []
# string = string.split()
# for i in string:
#     if i.isdigit():
#         prices.append(i)
#     else:
#         clothes.append(i)
# for i in range(len(clothes)):
#     # print(clothes[i], prices[i])
#     print(f'{clothes[i]} - {prices[i]}')


# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из букв и чисел.
# Создайте скрипт для сохранения пароля в файл password.txt.


# Задача 4. Считайте строковые данные из файла. Создайте словарь, содержащий все символы в файле


# data = open('dictionary.txt', encoding='utf-8')
# string1 = data.read()
# data.close()
# print(string1)
# new_dictionary = {}
# for i in string1:
#     new_dictionary[i] = i
# print(new_dictionary)



