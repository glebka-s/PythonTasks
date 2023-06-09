# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

def numbers (s, p):
    solution = ''
    if (s**2 < 4 * p) or (s < 0) or (p < 0):
        return 'Ошибка!'
    
    x1, y1, x2, y2 = 0, 0, 0, 0

    x1 = (s + (s**2 - 4 * p)**0.5) / 2
    y1 = s - x1

    x2 = (s - (s**2 - 4 * p)**0.5) / 2
    y2 = s - x2

    if x1 > 0 and y1 > 0:
        solution += str(x1) + ' ' + str(y1) + ' ; '
    if x2 > 0 and y2 > 0:
        solution += str(x2) + ' ' + str(y2)

    if solution == '':
        return 'Нет ответа'
    else:
        return solution

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

print(numbers(s, p))