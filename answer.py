dialog1=' '
def get_answer(question):
	answers={"привет":"И тебе привет!"," как дела ?":" Лучше всех","пока":" Увидимся"}
	return answers.get(question.lower(),'привет, попробуй еще раз')
while dialog1!='пока':	
	dialog1=input()
	print(get_answer(dialog1))

