age=int(input(' Пожалуйста введите свой возраст '))
if 6 > age > 0:
	print('Детский сад')
elif 17 >= age >= 6:
	print('Школа')
elif 22 >= age > 17:
	print('Институт')
else:
	print('Работа')	