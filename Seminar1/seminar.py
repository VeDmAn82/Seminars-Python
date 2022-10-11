# Семинар1

# Напишите программу, которая на вход принимает число и выдаёт его квадрат (число умноженное на само себя).

number = int(input('Введите число: '))
print(number**2)


# Задача1 Является ли одно число квадратом другого

numA = int(input("Введите число А: "))
numB = int(input("Введите число B: "))
if numA**2 == numB or numB**2 == numA:
    print("Число является квадратом")
else:
    print("Число не является квадратом")


# Задача2 Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди
# введённых чисел те, которые кратны трём

number = None
count = 0
while number != 0: 
    number = int(input("Введите число: "))
    if number % 3 == 0 and number != 0:
        count += 1
print("Ввод окончен")
print("Количество чисел кратных 3, равно ", count)


# Задача3 Напишите программу, которая будет на вход
## принимать число N и выводить числа от -N до N

import math
num = float(input("Введите число N: "))
num = abs(num)
x = math.floor(num)

for i in range(-x, x+1):   
    print(i, end= " ")


# Задача4 Напишите программу, которая будет принимать на вход дробь
## и показывать первую цифру дробной части числа

num = input("Введите дробное число: ")
print(num[num.find(".") + 1])


# Задача5 Напишите программу, которая находит наибольшее и
## наименьшее число из списка значений

num = [int(el) for el in input().split()]    # короткий вариант
print(f'max = {max(num)}')
print(f'min = {min(num)}')

numbers = [int(el) for el in input().split()]      # numbers = [1, 5, 3, 8, 2]         
max_el = min_el = numbers[0]
for number in numbers:
    if number > max_el:
        max_el = number
    elif number < min_el:
        min_el = number
# # print(numbers)                                   print(*numbers)   '*' - вывод без квадратных скобок
print(f'max = {max_el}')
print(f'min = {min_el}')




