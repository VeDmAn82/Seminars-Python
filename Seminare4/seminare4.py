# Задача 0. Создайте файл random.txt. Запишите в него 10 случайных чисел

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 10))
print(numbers)

data = open('random.txt', 'w')
data.writelines(str(numbers))
data.close()

with open('random.txt', 'a') as data:
    data.writelines(str(random))


# Задача 1. Создайте кортеж, заполненный случайными
# числами. Напишите метод, который заменяет элемент
# в кортеже по заданному индексу

def change_index(num, index):
    num = list(num)
    num[index - 1] = random.randint(10, 100)
    num = tuple(num)
    return num

size = random.randint(5, 12)
num = tuple(random.randint(10, 100)for i in range(size))     # Кортеж
print(num)
index = int(input('Введите индекс: '))
print(change_index(num, index))


# Задача 2. Актёров разделили на списки по трём качествам
# «умные», «красивые», «сильные». На главную роль нужен актёр
# обладающий всеми тремя качествами. Определите, сколько есть
# претендентов на главную роль. Списки актёров поместите в
# соответствующие файлы.
# 25 мин
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


def openFile(nameFile):
    f = open(nameFile, encoding='utf-8')
    phrase = f.readlines()
    f.close()
    list = phrase[0].split()
    return set(list)

beauty = openFile('beauty.txt')
strong = openFile('strong.txt')
smart = openFile('smart.txt')

print(beauty.intersection(smart).intersection(strong))


# Задача 3. Сгенерируйте список случайных чисел от
# 1 до 20, состоящий из 10 элементов. Удалите из
# списка дубликаты уже имеющихся элементов

# num = list(random.randint(1, 20)for i in range(10))     # tuple - Кортеж
# print(type(num), num)                                   # set - Множество
                                                          # list - Список

def GetNumbers():
    data = open("list.txt",'w')
    numbers = [random.randint(1,20) for i in range(0,10)]
    data.write(str(numbers))
    print(numbers)
    data.close()
GetNumbers()

def FindeDublicate():
    data = open("list.txt", "r", encoding="utf=8")
    num = data.readline()[1:-1].split(", ")
    num = [int(i) for i in num]
    num = set(num)
    print(num)
FindeDublicate()


# # Задача4. 

import math
radius = 15
print(round(math.pi * math.pow(radius, 2), 2))
