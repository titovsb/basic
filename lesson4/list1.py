'''
1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
    Примечание. Списки создайте вручную, например так:
'''

my_list_1 = [5, 5, 2, 2, 5, 8, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

#print(list(set(my_list_1) - set(my_list_2)))

for e in my_list_1[:]:
    if e in my_list_2:
        my_list_1.remove(e)

print(my_list_1)
