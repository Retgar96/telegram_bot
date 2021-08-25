import telebot
#Привет


bot = telebot.TeleBot('1775416764:AAE05rKKLfYuKdRKuh4ytffGMGsHED0Hsko')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
