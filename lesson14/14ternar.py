import random

listBase = [random.randint(-10, 10) for i in range(10)]
print(listBase)

def filterCustom(l):
    return [num if num < 0 else num**2 for num in l]

print(filterCustom(listBase))
print(listBase)
