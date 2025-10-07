#1
'''
x = str(input())
print(x[3])
'''
#2
'''
x = float(input())
sec = x%60
minn = (x%3600)//60
chas = x//3600
print(f'секунды {sec},минуты {minn},часы  {chas}')
'''
#3
'''
x = int(input())
print(x%2)
'''
#4
'''
x = int(input())
y = int(input())
n = int(input())
i = (x*100+y)*n
print(i//100,i%100)
'''
#5
'''
x = "(\___/)"
x2 = "(='.'=)"
x3 = '(")_(")'


n = int(input())
print((x+'')*n,(x2+'')*n,(x3+'')*n, sep='\n')
'''
#6
'''
x = input()
y = int(input())
z = int(input())
print((int(x*y))*z)
'''
#7
'''
raw = input('Enter number:')
print(raw)
'''
#8
'''
import math
a = int(input())
b = int(input())
c = int(input())

cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
cos_b =  (a**2 + c**2 - b**2) / (2 * a * c)
cos_c =  (a**2 + b**2 - c**2) / (2 * a * b)

print((math.acos(cos_a))*180/math.pi, (math.acos(cos_b))*180/math.pi,(math.acos(cos_c))*180/math.pi)
'''
#9
'''
ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())

a = ((COMP/ATT) - 0.3)*5
b = ((YDS/ATT)-3)*0.25
c = (TD/ATT)*20
d = 2.375 - ((INT/ATT)*25)

PAS = ((a+b+c+d)/6)*100
print(PAS)
'''

#10
'''
x= int(input())
y = int(input())
c = (x%y==0) or (y%x==0)
print(int(c))
'''
#11
'''
x = float(input())

chas = int(x//30)
minn = int((x/30-chas)*60)
print(chas ,minn)
'''
#12
'''
import datetime
x= datetime.date.today()
print(x)
'''
#13










