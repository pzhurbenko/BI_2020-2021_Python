# Подгружаем блок математики
import math
from random import randint

# Приветствие
print('Привет, это калькулятор.\n
Для вызова справки введите man вместо первого числа\n')

# Вводим первое число
while True:
    try:
        num1 = input('Первое число: ')

        if num1 == 'man':  # Вызов справки
            print('На ввод принимаются только рациональные числа\n 
            Поддерживаются следующие операции:\n 
            + сложение\n- вычитание\n* умножение\n/ деление\n 
            ^ возведение первого числа в степень второго\n 
            1/ извлечение из первого числа корня степени второго\n 
            log логарифм первого числа по основанию второго\n 
            ! факториал\n')
            esc = (input('Для выхода введите esc: '))

            while esc != 'esc':  # Выход из справки
                esc = (input('Для выхода введите esc: '))
            continue

        else:
            num1 = float(num1)
    except ValueError:
        print('Введите рациональное число!')
        continue
    else:
        break

# Операции над числами
while True:
    oper = input('Операция: ')
    conditions = ['+', '-', '*', '/', '^', '1/', 'log', '!']
    if oper in conditions:
        break
    else:
        print('Введите правильную операцию(смотри справку)')
    continue
if oper == '!':
    print('Ответ: ', math.factorial(num1))  # Рассчет факториала
else:

    # Вводим второе число
    while True:
        try:
            num2 = float(input('Второе число: '))
        except ValueError:
            print('Введите рациональное число!')
            continue
        else:
            break

    result = 0  # Переменная для записи результата

    if oper == '/' and num2 == 0:  # Делимость на ноль
        print('Вы пытаетесь разделить на ноль')

    else:  # Все операции

        if oper == '+':
            result = num1 + num2

        elif oper == '-':
            result = num1 - num2

        elif oper == '*':
            result = num1 * num2

        elif oper == '/':
            result = num1 / num2

        elif oper == '^':
            result = num1 ** num2

        elif oper == '1/':
            result = num1 ** (1 / num2)

        elif oper == 'log':
            result = math.log(num1, num2)

        # Вывод результата
        print('Ответ: ', result, '\n')

        # User friendly block
        if result == 666:
            print('Вы вызвали сотону')  # Это его любимое число
        elif result == 1:
            print('Это можно было посчитать и устно!')  # В самом деле
        else:
            random = randint(1, 7)
            if random == 1:
                print('Хочу считать ещё!')
            if random == 2:
                print('Красивое число!')
            if random == 3:
                print('И зачем тебе эта математика?')
            if random == 4:
                print('Это всего-лишь сухие цифры...')
            if random == 5:
                print('Ух, это было сложно посчитать!')
            if random == 6:
                print('Сегодня мне снились электроовцы')
            if random == 7:
                print('Надеюсь, это тебе поможет...')
