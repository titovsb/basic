import random


def ShowRandomElement(l):
    return random.choice(l)


if __name__ == '__main__':
    print(ShowRandomElement(range(10)))
