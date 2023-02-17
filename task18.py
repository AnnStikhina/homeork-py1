#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input())
list_1 = list()
for i in range (n):
    x = int(input())
    list_1.append(x)
k = int(input())
n = abs(k - list_1[0])
number = list_1[0]
for i in range (1, len(list_1)):
    if m > abs(list_1[i] - k):
        n = abs(list_1[i] - k)
        number = list_1[i]
print(number)
