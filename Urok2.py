# 1) Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")
print(f"Сумма цифр = {sumNums(num)}")

# 2) Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

# Задача 3. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

n = int(input("Введите число n: "))
s = 0
for i in range(1,n+1):
    s += (1+1/i)**i
print(f"Полученная сумма последовательности (1+1/n)^n равна {round(s,2)}")


# Задача 4. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs

# Задача 5. Реализовать алгоритм перемешивания списка.

import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")
