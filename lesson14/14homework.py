import random

fruitsOne = ['Яблоко', 'Груша', 'Мандарин', 'Персик', 'Лайм']
fruitsTwo = ['Яблоко', 'Личи', 'Апельсин', 'Лайм', 'Абрикос']

# Получить список фруктов, присутствующих в обоих исходных списках.
fruitsResult = [fru for fru in fruitsOne if fru in fruitsTwo]
print(fruitsResult)

# Дан список, заполненный произвольными числами.
nums = [random.randint(-20,20) for i in range(10)]
print(nums)

# все элементы кратны 3,
print([num for num in nums if not num%3])

# Элемент положительный,
print([num for num in nums if num > 0])

# Элемент не кратен 4.
print([num for num in nums if num%4])
