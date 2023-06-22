n = int(input('Введите натуральное число: '))
factorial = 1
while n > 0:
    factorial *= n
    n = n - 1
else:
    print(f'n! = {factorial}')
