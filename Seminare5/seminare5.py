# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100

import random

numbers = [random.randint(1, 100) for i in range(15)]
print(numbers)

for i in numbers:           # обычный способ
    if i % 5 == 0:
        print(i)

result = lambda x: x % 5 == 0

result = filter(result, numbers)      # через фильтр с выводом через *  
print(*result)

result = list(filter(result, numbers))  # через фильтр с преобразованием в список
print(result)



# Задача 1. На вход подаётся четырёхзначное число. Получите список, 
# состоящий из цифр данного числа, увеличенных на 10. 9650 –> [19, 16, 15, 10]

num = list(input('Введите четырехзначное число: '))
print(num)
result = lambda x: int(x) + 10
result = list(map(result, num))
print(result)



# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, 
# в результате которой некоторые данные не расшифровались. 
# Расшифруйте данные. Определите, в какой клетке находится лев. 
# Номер клетки совпадает с номером строки.
# (абвгдеёжзийклмнопрстуфхцчшщъыьэюя)

def ConvertToBinary(number):

    result = ''
    while number > 0:
        result = str(number%2) + result
        number = number // 2
    return result
    
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'          # '000001'

codeList = [ConvertToBinary(i) for i in range(len(alphabet))]   # объединение в одну строку 1 и 2 шага

codeList = [int(i) for i in range(len(alphabet))]     # 1) индексы алфавита от 0 до 32 
codeList = [ConvertToBinary(i) for i in codeList]     # 2) конвертация индексов из десятичной в двоичную системы
codeList = ['0'*(6-len(i))+i for i in codeList]       # 3) добавляем нули до 6 символов

dictionary = {}
for i in range(len(codeList)):
    dictionary[codeList[i]] = alphabet[i]
print(dictionary)

data = open('animals.txt', 'r')
animalsCodeList = data.readlines()
data.close()

for animal in animalsCodeList:
    for i in range(len(animal)//6):
        bias = i * 6
        print(dictionary[animal[bias:bias+6]], end = '')
    print()



# Задача 3. Имеется информация о том, телефонами каких компаний сейчас торгуют магазины.
# Определите те компании, чьи телефоны присутствуют в каждом магазине
    
data = open('telephones.txt', 'r')
phones = data.readlines()
data.close()

shop1 = set(phones[1].rstrip().split(', '))
shop2 = set(phones[3].rstrip().split(', '))
shop3 = set(phones[5].rstrip().split(', '))
print(shop1.intersection(shop2).intersection(shop3))



# Задача 4. Задайте список из 15 случайных чисел. Выведите все пары кратных чисел из этого списка

import random

numbers = [random.randint(1, 10) for i in range(15)]
print(numbers)

for i in range(len(numbers) - 1):
    for j in range(i+1, len(numbers)):
        if numbers[i] != numbers[j] and numbers[i] != 1 and numbers[j] != 1:
            if numbers[i] % numbers[j] == 0 or numbers[j] % numbers[i] == 0:
                print(numbers[i], numbers[j])
