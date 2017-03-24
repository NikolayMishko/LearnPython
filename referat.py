with open('referat.txt', 'r') as f:
	content = f.read()
	words=0
	pos='out'
	s=0
	in_out='out'
	content=content.replace('\n',' ')
	for letter in content:
		if letter != ' ' and pos =='out':
			words +=1
			pos = 'in'
		elif letter == ' ':
			pos = 'out'
	print(words+s)
