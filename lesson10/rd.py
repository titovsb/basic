import os


def RemoveDir():
    for i in range(1, 10):
        newPath = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        if not os.path.isdir(newPath):
            print(f'Каталог {newPath} не найден')
        else:
            os.rmdir(newPath)
            print(f'Каталог {newPath} удален')

    print(os.listdir())


if __name__ == '__main__':
    RemoveDir()
