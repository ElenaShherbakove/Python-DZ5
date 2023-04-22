# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

# *Пример:*

# 2 2
#     4

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(sum(a, b))