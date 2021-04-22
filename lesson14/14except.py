def exceptPow(val):
    if val != 13:
        return val**2
    else:
        raise ValueError('ошибка данных')

digit = int(input("Введите число: "))
try:
    print(exceptPow(digit))
except Exception as e:
    print(f'Обработка исключения: {e}')
else:
    print("Исключение не возникло")
finally:
    print("Привет из блока finnaly!")
print('Финиш')
