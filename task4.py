# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем
# Петя и Сережа вместе

S = int(input('S = '))
if S % 6 == 0:
    print(S // 6, ' ', S // 6 *4, ' ', S // 6)
else:
    print('Нельзя определить!')