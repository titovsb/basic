'''
3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого. ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
'''

import random
import time

# creatureStruct = {
#     'name': "",
#     'health': random.randint(50, 100),
#     'damage': random.randint(5, 40)
#
# player = {
#     'name': "",
#     'health': random.randint(50, 100),
#     'damage': random.randint(5, 40)
# }
# enemy = {
#     'name': "",
#     'health': random.randint(50, 100),
#     'damage': random.randint(5, 40)
# }

def InitCreature (nameCreature):
    '''Создаем животное со известным именем и случайными данными'''
    name = input('Дайте имя созданию ({}) или нажмите ввод чтобы оставить по умолчанию: '.format(nameCreature))
    return {'name': nameCreature if name == '' else name,
            'health': random.randint(50, 100),
            'damage': random.randint(5, 15) }

def PrintStatusArgs(msg, *creatureList):
    print(msg)
    for creature in creatureList:
        print(f"Создание: {creature['name']}, здоровье: {creature['health']}, урон: {creature['damage']}")

def CheckDamage(player1, player2):
    '''Возвращаем истину если бой продолжается. Сообщяем о победе.'''
    def OutWin(player):
        print(f"Выиграл боец {player['name']}. Победа")
    ret = False
    if player1['health'] < 0:
        OutWin(player2)
    elif player2['health'] < 0:
        OutWin(player1)
    else:
        print("Противники сильны и бой продолжается")
        ret = True
    return ret

def Attacked(whoAttacked):
    '''Атакуем. Параметр true = first атакует second'''
    global first
    global second
    print(f"{first['name'] if whoAttacked else second['name']} атакует")
    def Attack(agressor, victim):
#        print(f"victim['health'] {victim['health']} - agressor['damage'] {agressor['damage']}")
        return victim['health'] - agressor['damage']
    if whoAttacked:
        second['health'] = Attack(first, second)
    else:
        first['health'] = Attack(second, first)

first = InitCreature('Человек')
second = InitCreature('Приведение')

PrintStatusArgs("Состояние новых игроков перед боем:", first, second)

while CheckDamage(first, second):
    Attacked(bool(random.randint(0,1)))
    PrintStatusArgs('Бой проведен, зализываем раны и осматриваем повреждения.',first, second)
    time.sleep(1)


