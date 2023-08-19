#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6428858866:AAEY4rJikW4XDZY-UtvW82DZXgPp3SrxFH8'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('привет.jpg', 'rb')
    bot.send_photo(message.chat.id, sti)

    #клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Смешной котик")
    item2 = types.KeyboardButton("Грустный котик")
    item3 = types.KeyboardButton("Влюбленный котик")
    item4 = types.KeyboardButton("Злой котик")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Привет, {0.first_name}! Здесь все очень просто. Нажми на кнопку и получишь котика".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Смешной котик':
            with open('смешной.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'Грустный котик':
            with open('грустный.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'Влюбленный котик':
           with open('влюбленный.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'Злой котик':
            with open('злой.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, 'Не знаю что ответить😢')

bot.polling(none_stop=True)
