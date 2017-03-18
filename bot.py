from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("362072092:AAEdbOCaRu2p44UVoUkHwZ05YkTKV3H0WM4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count))
    

    #dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me_new))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')    

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def show_error(bot, update, error):
    print(error) 

def get_answer(question):
    answers={"привет":"И тебе привет!"," как дела ?":" Лучше всех","пока":" Увидимся"}
    if question[-1]=='=':
        print('Давай разберемся')
        print(calculator(question))
        return calculator(question)
    else:
        return answers.get(question.lower(),'привет, попробуй еще раз')
def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def talk_to_me_new(bot, update):
    bot.sendMessage(update.message.chat_id,get_answer(update.message.text))

def planet(planet_name):
	bot.sendMessage(update.message.chat_id,'Тест')


#s=input('Введите фразу ')
def word_count(bot, update):
	s=update.message.text
	s1=s[11:]
	print(s1)
	print('Вызван word_count')
	if len(s1)>0:
		if (s1[0]=='"') and (s1[-1]=='"') and len(s1)>0:
			m=len(s1.split(' '))
			bot.sendMessage(update.message.chat_id,m)



def calculator(question):
    print('calc')
    s=question
    if s[-1]=='=':
        l=('Произошла какая-то ошибка')
        s=s[:-1]
        a=(s.find('/'))
        b=(s.find('*'))
        c=(s.find('+'))
        d=(s.find('-'))
        if a!=-1:
            sign='/'
            poz=a
            s1=int(s[:poz])
            s2=int(s[(poz+1):])
            if s2==0:
                l='Делить на 0 нельзя'
            else:
                l=s1/s2
        elif b!=-1:
            sign='*'
            poz=b
            s1=int(s[:poz])
            s2=int(s[(poz+1):])
            l=s1*s2
        elif c!=-1:
            sign='+'
            poz=c
            s1=int(s[:poz])
            s2=int(s[(poz+1):])
            l=s1+s2
        elif d!=-1:
            sign='-'
            poz=d
            s1=int(s[:poz])
            s2=int(s[(poz+1):])
            l=s1-s2
        else:
            print('знак не введен')

    return l
main()