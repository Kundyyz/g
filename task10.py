# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
reshka = 0
orel = 0
print('Если решка введите: 1')
print('Если орел введите: 0')
for i in range(n):
    moneta = int(input('Монета: '))
    if (moneta != 0) and (moneta != 1):
        n += 1
        print('Неправильные значения!')
    elif (moneta > 0):
            reshka += 1
    else:
            orel += 1
if reshka > orel:
    print(f'Минимальное количество монет, которые нужно перевернуть: {orel}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть: {reshka}')    
