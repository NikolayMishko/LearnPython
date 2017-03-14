fname=input('Кто вам нужен ? ')

def find_person(fname):
	name=' '
	name_list=["Вася","Маша","Петя","Валера","Саша","Даша"]
	while name!=fname:
		if len(name_list)==0:
			print(str(fname)+' не в списке')
			break
		name=name_list.pop()
	if name==fname:
		print(name+' тут')
find_person(fname)
