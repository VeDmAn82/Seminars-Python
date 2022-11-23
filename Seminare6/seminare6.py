# Задача 0. Дан список случайных элементов. Проверьте, что все его элементы уникальны

import random

def zadacha0():
    size = 4
    numbers = [random.randint(1, 10) for i in range(size)]
    print(numbers)
    print('все элементы уникальны' if len(numbers) == len(set(numbers)) else 'есть совпадающие элементы')



# Задача 1. Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр

def CheckNumber(number):
    return 10000 <= number <= 99999

def CountAllElements(number):
    number = str(number)
    number = set((i, number.count(i)) for i in set(number))
    print(number)
    return number

def zadacha1():    
    numberFirst = 55234
    numberSecond = 23455

    if CheckNumber(numberFirst) and CheckNumber(numberSecond):
        numberFirst = CountAllElements(numberFirst)
        numberSecond = CountAllElements(numberSecond)
        print('yes' if numberFirst == numberSecond else 'no')
    else:
        print('Числа не удовлетворяют условию')
zadacha1()



# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. Приоритет операций стандартный
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких действий
# в) Решите задачу средствами python

# a)
def sum(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

formula = '20*33'
formula = list(formula)
formulaElements = []
number = ''
operator = ''

for i in formula:
    if i.isdigit():
        number += i
    else:
        formulaElements.append(int(number))
        operator = i
        number = ''
formulaElements.append(int(number))        
print(formulaElements)
print(operator)
operations = \
    {
        '+': sum(formulaElements[0], formulaElements[1]),
        '-': formulaElements[0] - formulaElements[1],
        '*': mult(formulaElements[0], formulaElements[1]),
    }
print(operations[operator])

# в)
def sum(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def zadacha2():
    formula = '1 + 20 * 33 / 33 - 7'
    print(formula, '=', eval(formula))



# Задача 3. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?

def zadacha3():
    bullPrice = 100
    cowPrice = 50
    calfPrice = 5
    money = 1000

    for bullCount in range(money//bullPrice):
        for cowCount in range(money//cowPrice):
            for calfCount in range(money//calfPrice):
                if bullCount + cowCount + calfCount == 100 and bullCount * bullPrice + cowCount * cowPrice + calfCount * calfPrice == 1000:
                    print(f'быки {bullCount}, коровы {cowCount}, телята {calfCount}')



# Задача 4. Дан список, выведите его первый и последний элементы

def zadacha4():
    size = 10
    numbers = [random.randint(1, 10) for i in range(size)]
    print(numbers)
    print(numbers[0], numbers[-1])
zadacha4()



