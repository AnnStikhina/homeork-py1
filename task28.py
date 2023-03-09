# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def sum(A, B):
    if (B==0):
        return A
    else:
        return sum(A+1,B-1)

a = int(input('Input A>>'))
print()
b = int(input('Input B>>'))
print()
if (a>=b):
    print (sum(a,b))
else:
    print(sum(b,a))