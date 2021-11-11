import telebot
from telebot import types

TOKEN="2109574372:AAHg2q9CMCy0XAaI0-s1VMvOn1LHvnIeMMo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Информация')
    item2 = types.KeyboardButton('Фото')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Информация':
            bot.send_message(message.chat.id, 'Напишите информацию')

        elif message.text == 'Фото':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            bot.send_message(message.chat.id, 'Отправьте фотографию в виде файла')
            
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Информация')
            item2 = types.KeyboardButton('Фото')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Главная', reply_markup = markup)        


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    src = 'uploads/' + file_info.file_path
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Ваша информация принята")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = r'C:\Users\Sp-center.uz\Desktop\elegram\uploads' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            bot.reply_to(message, "Ваша информация принята")
    except Exception as e:
       bot.reply_to(message, e)





bot.polling(none_stop = True)