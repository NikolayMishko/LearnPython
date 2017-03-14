answer=' '
def get_answer():
	print('Давай сначала разберемся все ли у тебя хорошо')

def ask_user(answer):
	while answer!='Хорошо':
		answer=input('Как дела? ')
		if answer[-1]=='?':
			get_answer()
ask_user(answer)