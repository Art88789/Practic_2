#1
'''
total_cost = float(input("Введите общую стоимость часов (в рублях): "))
silver_hours_count = 96 
silver_hour_price = 48    
gold_hours_count = silver_hours_count // 16  
silver_total_cost = silver_hours_count * silver_hour_price
gold_total_cost = total_cost - silver_total_cost
gold_hour_price = gold_total_cost // gold_hours_count
print(f"Стоимость одного: {int(gold_hour_price)}")
'''

#2
'''
x = input()
print(*x.split(), sep='\n')
'''

#3
'''
x = input()
fly= x.split()
f1 = float(fly[0])
f2 = float(fly[1])
print(f1+f2)
'''
#4
'''
x=int(input('Жен'))
y = int(input('Пакетов у одной жены'))
z = int(input('кошек в пакете'))
o = int(input('Котят у кошек'))
print((x*y*z*o)+(x*y*z)+x+1)
'''
#5
'''
x = float(input())
y = x*0.19
print(str(y)[:-2])
'''
#6
'''
funt=float(input())
dui=float(input())
print(str((funt/(dui**2))*704.5)[:-2])
'''
#7
'''
gek = 1
sm =1
met_geka = gek * 10000
met_sma = sm/100
kub_met = met_geka*met_sma
lit = kub_met*1000
print(lit)
print()
'''
#8
'''
x = float(input())#всего
y= float(input())#друзья
print(x//(y+1))
'''
#9
'''
poimal = float(input())
semei = float(input())
print(poimal%semei)
'''
#10
'''
mil=1609
x = int(input())
print(x//mil)
'''
