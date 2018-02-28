import config
import telebot

bot = telebot.TeleBot(543611577:AAES1h_PSRr_IQroA2rRpGLGV5IlYgxZkZ0)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
