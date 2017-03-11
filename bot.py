from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("362072092:AAEdbOCaRu2p44UVoUkHwZ05YkTKV3H0WM4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

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
	return answers.get(question.lower(),'привет, попробуй еще раз')    

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def talk_to_me_new(bot, update):
	#print('Wazaaaaaap')
    bot.sendMessage(update.message.chat_id,get_answer(update.message.text))

main()