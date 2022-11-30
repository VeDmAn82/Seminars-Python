# Задача 1. Задайте двумерный массив случайных чисел размером 4х5. Случайные числа не должны
# повторяться. Запишите массив в txt-файл

import random

def printMatrix(numbers):
    for row in numbers:
        print(row)

def zadacha1():
    rows = 4
    columns = 5
    numbers = [0] * rows
    used = []
    for i in range(len(numbers)):
        numbers[i] = list(0 for _ in range(columns))
    for i in range(rows):
        for j in range(columns):
            current_number = random.randint(0, 30)
            while current_number in used:
                current_number = random.randint(0, 30)
            numbers[i][j] = current_number
            used.append(current_number)
    return numbers
    # a = numbers[0]
    # print(a)
    # print(a[3])
    # print(numbers[0][3])

    

# Задача 2. Считайте двумерный массив из файла. Найдите разницу между вторым максимальным и
# вторым минимальным элементами массива

def zadacha2():
    numbers = zadacha1()
    printMatrix(numbers)

    result = []
    for row in numbers:
        for el in row:
            result.append(el)
    print(result)
    # result = list(set(result))   # сортировка через set
    result.sort()                  # сортировка через метод sort
    print(result)
    print(result[1], result[-2])
    print(f'{result[-2]} - {result[1]} = {result[-2] - result[1]}')

zadacha2()



# Задача 3. В зрительном зале 25 рядов, в каждом из которых 36 мест. Информация о проданных билетах должна
# храниться в виде двумерного массива, в котором номера строк соответствуют номерам
# рядов, а номера столбцов – номерам мест. Определите, где лучше сесть компании из M человек, если они хотят
# ряды только с K-го по N-ный. Все люди должны быть рядом после посадки.
# Если это невозможно, вывести соответствующее сообщение

import numpy as np

seats = np.random.randint(2, size=(25, 36))

print(seats)

M = int(input('How many people: '))
K = int(input('The closest row: '))
N = int(input('The farthest row: '))
found = False

for i in range(K, N + 1):
    for j in range(36 - M + 1):
        if 1 not in seats[i, j : j + M + 1]:
            print(seats[i, j : j + M])
            print(i + 1, j + 1)
            found = True
        if found:
            break
    if found:
        break
else:
    print('No seats')



# Задача 4. Дан двумерный массив. Определите номер строки и столбца, в котором находится
# максимальный элемент

# Вариант 1:
import numpy as np

numbers = np.random.randint(500, size=(10, 15))

print(numbers)

max_i = 0
max_j = 0

for i in range(numbers.shape[0]):
    for j in range(numbers.shape[1]):
        if numbers[i, j] > numbers[max_i, max_j]:
            max_i, max_j = i, j

print(max_i, max_j)

# Вариант 2:
def zadacha4():
    numbers = zadacha1()
    printMatrix(numbers)
    result = []
    for row in numbers:
        for el in row:
            result.append(el)

    maximum = max(result)
    print(f'максимум равен {maximum}')
    max_index = result.index(maximum)
    print(f'его индекс равен {max_index}')
    rows = len(numbers)
    columns = len(numbers[0])
    print(max_index // columns)
    print(max_index % columns)

zadacha4()

