import datetime 
from datetime import *
a=datetime.now()
#print(a)
n=a.strftime('%d %m %Y')
d1=timedelta(days=-1)
a1=a+d1
n1=a1.strftime('%d %m %Y')
d2=timedelta(days=-28)
a2=a+d2
n2=a2.strftime('%d %m %Y')
print('Вчера было: '+str(n1))
print('Сегодня: '+str(n))
print('Месяц назад: '+str(n2))
st="01/01/17 12:10:03.234567"
date_dt = datetime.strptime(st, '%y/%m/%d %H:%M:%S.%f')
print(date_dt)