# Найдите сумму цифр трехзначного числа.

def sum_numbers(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

number = int(input('Введите трёхзначное число:'))
print(sum_numbers(number))