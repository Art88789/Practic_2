#1
'''
x = input()
if x == 'пароль' or x ==
'Пароль':
    print('Проходи')
else:
    print('Доступ запрещен')
'''
#2
'''
x = input()
y = input()
if (x=='Примите' or x == 'примите') and( y =='Программу' or y == 'программу'):
    print('верно')
else:
    print('неверно')
'''
#3
'''
print('Как зовут главного персонажа романов Яна Флеминга о вымышленном шпионе секретной разведывательной службы Великобритании?')
x = input()
if x == 'Уильям Сомерсет Моэм' or x == 'уильям сомерсет моэм':
    print('верно')
else:
    print('неверно')
'''
#4
'''
print('вы поедете на бал?')
x = input()
if x =='нет' or x=='да':
    print('неверно')
else:
    print('верно')
'''
#5
'''
x == int(input())
y == int(input())
if x>y:
    print(y)
else:
    print(x)
'''
#6
'''
x = input('Введите счет через ":" ')
y,u = x.split(':')
y1 = int(y)
u1 = int(u)
if y1>u1:
    print('1 команда')
elif y1<u1:
    print('2 команда')
else:
    print(0)
'''
#7
'''
x = input()
y,y1,y2 = x.split(' ')
u=int(y)
u1 = int(y1)
u2 = int(y2)
if u>u1 and u>u2:
    print(u)
elif u1>u2:
    print(u1)
else:
    print(u2)
'''
#8
'''
print('Как зовут?')
x= input()
print(f'Приятно,{x}. Меня Марк')
print('Сколько лет?')
y=int(input())
if y>78:
    print(f'Вы старше на {y-78}')
else:
    print(f'Я вас старше на {78-y}')
print('вам нравится прогать?')
u = input()
if u=='нет':
    print('Жаль')
elif u=='да':
    print('Ураа')
'''
#9
'''
print('Собака короткошерстной породы?')
x=input()
if x=='да':
    print('Рост собаки менее 50 см?')
    y=input()
    if y=='да':
        print('У собаки короткий хвост?')
        u=input()
        if u=='да':
            print('Английский бульдог')
        else:
            print('У собаки длинные уши?')
            a = input()
            if a=='да':
                print('гончая')
            else:
                print('у собаки короткое тело?')
                s= input()
                if s=='да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        print('Собака весит более 50 кг?')
        i =input()
        if i=='да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    print('Рост собаки менее 50 см?')
    z=input()
    if z=='да':
        print('У собаки доброжелательный характер?')
        o=input()
        if o =='да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')

    else:
        print('У собаки рост меньше 70 см?')
        p=input()
        if p=='да':
            print('у собаки длинные уши?')
            d = input()
            if d=='да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            print('Окрас ражий с белыми отметинами?')
            f = input()
            if f=='да':
                print('сенбернар')
            else:
                print('Белоснежный окрас?')
                g = input()
                if g=='да':
                    print('ирладский волкодав')
                else:
                    print('ньюфаундлен')

'''
#10
'''
x = int(input('Сколько шестеренок?'))
if x%2==0:
    print('Можно')
else:
    print('Нельзя')
'''
