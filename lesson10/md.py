import os

def MakeDir():
    for i in range(1, 10):
        newPath = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        if os.path.isdir(newPath):
            print(f'Каталог {newPath} уже существует')
        else:
            os.mkdir(newPath)
            print(f'Каталог {newPath} создан')

    print(os.listdir())

if __name__ == '__main__':
    MakeDir()
