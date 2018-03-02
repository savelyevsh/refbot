import telebot
use = []
user = []
user_count = []

bot = telebot.TeleBot("514242392:AAE0QXg8ZoOf9bk-vvAwFTpaTLqQX8qJvAw")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    uid = message.from_user.id
    mes = message.text
    print(mes)
    print(uid)
    print(len(mes))
    print(mes[1:6])
    print(use)
    print(user)
    print(mes[7:])
    if len(mes) > 5:
        print(1)
        if mes[:6] == '/start':
            print(2)
            try:
                uid1= int(mes[7:])
                print(3)
                if uid in use:
                    bot.send_message(message.from_user.id, 'vi ushe prisoedinilis k nam')
                    print(4)
                else:
                    user.append(uid)
                    user_count.append(0)
                    print(5)
                    use.append(uid)
                    n = user.index(uid1)
                    user_count[n] += 1
                    bot.send_message(message.from_user.id, 'privet bro, vot ref sisteama')
                    if user_count[n] > 1:
                        print(6)
                        bot.send_message(uid1, 'vot tvoya ssilka^ dkfjslfjklds')
                    else:
                        print(7)
                        bot.send_message(uid1, 'ostalos priglasit' + str(2 - user_count[n]) + 'userov')
                        
            except:
                print(8)
                bot.send_message(uid, 'vasha_ref ssilka = https://telegram.me/ref_pumpbot?start='+ str(uid))
    else:
        print(9)
        bot.send_message(uid, 'vasha_ref ssilka = https://telegram.me/ref_pumpbot?start='+ str(uid))
    print(use)
    print(user)
    print(user_count)
