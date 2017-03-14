list=[{'school_class': '4a', 'scores': [3,3,3,3,3,3,3,3,3,3,3,3]},{'school_class': '4b', 'scores': [3,4,5,2,3,5,3,5,5,5,2,5,5,3,2]},{'school_class': '5a', 'scores': [3,3,3,3,3,5,3,4,4,4,2,5,5,3,2]},{'school_class': '5b', 'scores': [3,4,4,4,4,4,3,4,4,4,2,5,5,3,2]},{'school_class': '6a', 'scores': [3,3,5,3,3,5,3,4,4,4,2,2,2,2,2]},{'school_class': '7a', 'scores': [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]}]
i=0
sum=0
res=0
y=0
for w in list:
	sum=0
	i=0
	print('Класс '+ w['school_class'])
	for x in w['scores']:
		sum=x+sum
		i=i+1
	print('Средняя оценка по классу ' + str(sum/i))
	res=res+sum	
	y=y+i
print('Средняя оценка по школе '+ str(res/y))     	


