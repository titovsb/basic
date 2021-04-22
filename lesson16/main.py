from core import mc_list, mc_help, mc_chdir, mc_makedir, mc_makefile, mc_delete, mc_copy, mc_game
import sys

mc_helpList = {
    'help': 'Помощь',
    'list': 'Список файлов и папок',
    'cd': 'Перейти в каталог от текущего ',
    'makedir': 'Создать папку',
    'makefile': 'Создать файл',
    'delete': 'Удалить файл или папку',
    'copy': 'Копировать file1 в file2',
    'game': 'Поиграть'
}

def isOneArgs(args):
    return True if len(args) > 1 else False

def isTwoArgs(args):
    return True if len(args) > 2 else False

if __name__ == '__main__':
    del sys.argv[0]
    if sys.argv:
        cmd = sys.argv[0]
        param1 = [] if len(sys.argv) <= 1 else sys.argv[1]
        param2 = [] if len(sys.argv) <= 2 else sys.argv[2]
        print("ПАРАМЕТРЫ",param1, param2)
        if cmd == 'help':
            mc_help(mc_helpList)
        elif cmd == 'list':
            mc_list()
        elif cmd == 'cd' and param1:
            mc_chdir(sys.argv[1])
        elif cmd == 'makedir' and param1:
            mc_makedir(sys.argv[1])
        elif cmd == 'makefile' and param1:
            mc_makefile(sys.argv[1])
        elif cmd == 'delete' and param1:
            mc_delete(sys.argv[1])
        elif cmd == 'copy' and param1 and param2:
            mc_copy(sys.argv[1], sys.argv[2])
        elif cmd == 'game':
            mc_game()
        else:
            print('Неизвестная команда или неверный синтаксис')
    else:
        print('Наберите "main.py help" для всех команд')
