answer=' '
def get_answer():
	print('Давай сначала разберемся все ли у тебя хорошо')

def ask_user(answer):
	try:
		while answer!='Хорошо':
			answer=input('Как дела? ')
			if answer=='':
				print('Что молчишь?')
			elif answer[-1]=='?':
				get_answer()	
	except KeyboardInterrupt:
		return print("\nЛадно, ладно, только без рук, я же шучу")			
ask_user(answer)