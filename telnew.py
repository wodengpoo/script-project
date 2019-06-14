import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openAPI

my_token = '819022289:AAE9plxU-hNEeHamxxNf9FRUoh1VjYfrdSw'

#bot = telegram.Bot(token=my_token)

#updates = bot.getUpdates()

#bot.sendMessage(chat_id = 681041711, text="안녕 나 때문에 고생이많아~")

def replyAptData(keyword, update):
    res_list = openAPI.Sgetsttn(keyword)
    print(res_list)
    msg = ''
    for r in res_list:
        for i in r:
            print(i)
            msg += i[0]
    if msg:
        update.message.reply_text(msg)
        print(msg)
    else:
        update.message.reply_text('%s 키워드에 해당하는 데이터가 없습니다.' % keyword)

def get_message(bot, update) :
    #update.message.reply_text("got text")
    #update.message.reply_text(update.message.text)

    text = update.message.text
    args = text.split(' ')
    if args[0] and len(args) > 1:
        print('정류소', args[1])
        replyAptData(args[1], update)
    else:
        update.message.reply_text('pardon?\n키워드 인식오류..')


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=False)
updater.idle()