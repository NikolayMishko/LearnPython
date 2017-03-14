string1=str(input('Введите строку 1 '))
string2=str(input('Введите строку 2 '))
def string_comparation(string1,string2):
	if string1==string2:
		return('1')
	if string1!=string2 and (len(string1)>len(string2)):
		return('2')
	if string1!=string2 and string2=='learn':
		return('3')
print(string_comparation(string1,string2))