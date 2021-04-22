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
    mc_game()
