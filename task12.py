# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

def numbers (s, p):
    solution = ''
    if (s**2 < 4 * p) or (s < 0) or (p < 0):
        return 'Ошибка!'
    
    elif (s**2 - 4 * p)**0.5 > s and s / 2 - ((s**2 - 4 * p)**0.5) / 2 > 0: # x > 0 and y > 0
        solution =  str(s + ((s**2 - 4 * p)**0.5) / 2) + \
        ' ' + str(s / 2 - ((s**2 - 4 * p)**0.5) / 2)

    elif (s**2 - 4 * p)**0.5 < s:

        if s / 2 - ((s**2 - 4 * p)**0.5) / 2 <= 0:
            solution = str(s - ((s**2 - 4 * p)**0.5) / 2) + \
            ' ' + str(s / 2 + ((s**2 - 4 * p)**0.5) / 2)
        
        elif s / 2 - ((s**2 - 4 * p)**0.5) / 2 > 0:
            solution = str(s - ((s**2 - 4 * p)**0.5) / 2) + \
            ' ' + str(s / 2 + ((s**2 - 4 * p)**0.5) / 2) + \
            ' ; ' + str(s + ((s**2 - 4 * p)**0.5) / 2) + \
            ' ' + str(s / 2 - ((s**2 - 4 * p)**0.5) / 2)
    
    if solution == '':
        return 'Нет ответа'
    else:
        return solution

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

print(numbers(s, p))