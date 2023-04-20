# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

def norm(x, y):
    return ((x - y)**2)**0.5

n = int(input('Введите размер массива: '))
list = []

for _ in range(n):
    list.append(int(input()))

x = int(input('Введите число: '))

min_norm = norm(x, list[0])
element_index = 0

for i in range(1, len(list)):
    if norm(x, list[i]) < min_norm:
        min_norm = norm(x, list[i])
        element_index = i

print(list[element_index])
