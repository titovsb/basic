'''
1. В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
'''

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