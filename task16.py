# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input())
list_1 = list()
for i in range (n):
    x = int(input())
    list_1.appennd(x)
count = 0
k = int(input())
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
