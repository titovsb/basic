import os
import shutil


def mc_list():
    print(os.listdir())


def mc_help(l):
    for k, v in l.items():
        print(f'{k} - {v}')


def mc_chdir(newpath):
    if newpath:
        try:
            os.chdir(newpath)
        except FileNotFoundError:
            print(f'Невозможно перейти в каталог {newpath}')
        else:
            print(f'Новый каталог {os.getcwd()}')
    else:
        print(f'Текущий каталог {os.getcwd()}')


def mc_makedir(name):
    if os.path.isdir(name):
        print(f'Каталог {name} уже существует')
    else:
        os.mkdir(name)
        print(f'Каталог {name} создан')


def mc_makefile(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(f'{text}\n')
    print(f'Файл {name} создан.')


def mc_delete(name):
    if name in os.listdir():
        if os.path.isdir(name):
            os.rmdir(name)
            print(f'Каталог {name} удален')
        else:
            os.remove(name)
            print(f'Файл {name} удален')
    else:
        print(f'Каталог или файл {name} не найден')


def mc_copy(name, newname):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, newname)
        except FileExistsError:
            print(f'Каталог {newname} уже существует')
        else:
            print(f'Каталог {name} скопирован в {newname}')
    else:
        shutil.copy(name, newname)
        print(f'Файл {name} скопирован в {newname}')

def mc_game():
    print('Загадайте число от 1 до 100 и нажмите ввод. Я буду угадывать.')
    input()

    start, finish = 1, 100

    whileCond = True

    while whileCond:
        computedNumber = (finish - start) // 2 + start
        print(f'Я думаю, что {computedNumber}, то что вы загадали')
        command = input('Оно меньше "<", больше ">" или равно "=" чем вы загадали? ')
        if command == "<":
            start = computedNumber
        elif command == ">":
            finish = computedNumber
        else:
            whileCond = False
    else:
        print('Я рад что угадал задуманное число')


if __name__ == '__main__':
    pass
    # mc_list()
    # mc_help()
    # mc_makedir('temp')
    # mc_makefile('test.txt', 'some text')
    # mc_delete('temp')
    # mc_delete('test2.txt')
    # mc_copy('temp', 'temp2')
    # mc_copy('test.txt', 'test2.txt')
    # mc_chdir('')
