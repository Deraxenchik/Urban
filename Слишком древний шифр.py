def password(n):
    result = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result
print('Введите число: ')
n = int(input())
if 3 <= n <= 20:
    print('Пароль: ', password(n))
else:
    print('Неверное значение')
