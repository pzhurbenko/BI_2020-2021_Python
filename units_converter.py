print('Конвертор физических величин, edittion 2.0\nВыберите величину: Давление, Сила, Радиоактивность\n')

# Поле для выбора величины
while True:
    ism = input('Введите величину: ')
    conditions = ['Давление', 'Сила', 'Радиоактивность']
    if ism in conditions:
        break
    else:
        print('Введите значение из списка')
    continue

# Величины
if ism == 'Давление':
    while True:
        try:
            push = float(input('Введите значение (Па): '))
        except ValueError:
            print('Введите число!')
            continue
        else:
            break
    print('Атмосфера: ', push * 101325)
    print('Водяной столб: ', push * 9.80665)
    print('Ртутный столб: ', push * 133.3223684)

elif ism == 'Сила':
    while True:
        try:
            push = float(input('Введите значение (H): '))
        except ValueError:
            print('Введите число!')
            continue
        else:
            break
    print('Тонна-сила: ', push * 9806.65)
    print('Дина: ', push * 0.00001)
    print('Тонна-сила, короткая [США]: ', push * 8896.443230521)
    print('Фунт-сила: ', push * 4.4482216152605)
    print('Унция-сила: ', push * 0.27801385095378125)
    print('Фунтал: ', push * 0.138254954376)

elif ism == 'Радиоактивность':
    while True:
        try:
            push = float(input('Введите значение (Бк): '))
        except ValueError:
            print('Введите число!')
            continue
        else:
            break
    print('Микрокюри: ', push * 3700)
    print('Милликюри: ', push * 3700000)
    print('Кюри, короткая [США]: ', push * 3700000000)

