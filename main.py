x = input('введите пароль: ')
if x == 'пароль':
    print('Проходи!')
else:
    print('Доступ запрещен!')


print('Какие два слова передал первой радиограммой Александр Попов?')
x = input('Первое слово: ')
y = input('Второе слово: ')
if x == 'Генрих' and y == 'Герц':
    print('Верно')
else:
    print('Неверно')


print('Как зовут главного персонажа'
      ' романов Яна Флеминго о вымышленном шпионе секретной разведывательной службы Великоритании')
x = input('Имя персонажа: ')
if 'ДЖЕЙМС БОНД' in x.upper() or 'АГЕНТ 007 ' in x.upper():
      print('Верно')
else:
      print('Неверно')


print('Вы поедете на бал?')
x = input('Ответ: ')
if x.lower() != 'да' and x.lower() != 'нет':
    print('Верно')
else:
    print('Неверно')


x, y = map(int, input().split())
if x > y:
    print(y)
else:
    print(x)


x, y = map(int, input().split(':'))
if x > y:
    print('1')
if x == y:
    print('0')
if x < y:
    print('2')


x, y, z = map(int, input().split())
if x > y and x > z:
    print(x)
if x < y and y > z:
    print(y)
if z > x and z > y:
    print(z)


x = input('Здравствуйте! Как вас зовут? ')
print(f'Очень приятно, {x}! Меня зовут Марк.')
y = int(input('Сколько Вам лет? '))
if y > 78:
    print(f'Да, {x}, Вы старше меня на {y - 78} лет.')
if y < 78:
    print(f'Да, {x}, я старше Вас на {78 - y} лет')
if y == 78:
    print(f'Да, {x}, мы с вами одного возраста.')
z = input('Вам нравится программировать? ')
if "ДА" in z.upper():
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
if "НЕТ" in z.upper():
    print('Жалью Я думал, Вы сможете написать интересную программу для меня.')


q = input('Собака короткошерстной породы? ')
if 'да' in q.lower():
    w = input('Рост собаки менее 50 см? ')
    if 'да' in w.lower():
        e = input('У собаки короткий хвост? ')
        if 'да' in e.lower():
            print('английский булдьог')
        else:
            t = input('У собаки длинные уши? ')
            if 'да' in t.lower():
                print('гончая')
            else:
                u = input('У собаки короткое тело? ')
                if 'да' in u.lower():
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        r = input('Собака весит более 50 кг? ')
        if 'да' in r.lower():
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    w = input('Рост собаки менее 50 см? ')
    if 'да' in w.lower():
        i = input('У собаки доброжелательный характер? ')
        if 'да' in i.lower():
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        o = input('У собаки рост менее 70 см? ')
        if 'да' in o.lower():
            p = input('У собаки длинные уши? ')
            if 'да' in p.lower():
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            a = input('Окрас рыжий с белыми отметинами? ')
            if 'да' in a.lower():
                print('сенбернар')
            else:
                s = input('Белоснежный окрас? ')
                if 'да' in s.lower():
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')


x = int(input())
if x % 2 == 0:
    print('да')
else:
    print('нет')
