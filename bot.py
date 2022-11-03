from telegram.ext import Updater,  MessageHandler, Filters

def echo (update,context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    like = 0
    
    if text == '👍':
        like+=1
    if text == '👍':
        text = f'"LIKE {k}: 👍 DISLIKE 5: 👎"'
    print(k)


    bot.sendMessage(chat_id,text)

updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()