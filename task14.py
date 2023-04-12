def powers (n):
    if n < 1:
        return 'Ошибка!'
    elif n < 2:
        return '1'
    else:
        solution = '1'
        i = 1
        while 2**i <= n:
            solution += ', ' + str(2**i)
            i += 1
    return solution

n = int(input('Введите число: '))
print(powers(n)) 

