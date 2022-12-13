
import telebot
import requests
import time

# 5821072722:AAEbVsW-Yp_soyzja3Gt99Fy7kZ975CvEJ0
bot = telebot.TeleBot("5821072722:AAEbVsW-Yp_soyzja3Gt99Fy7kZ975CvEJ0", parse_mode=None)    # Создание телебота


@bot.message_handler(content_types=["text"])
def hello_user(message):
    if 'привет' in message.text:                           # Задача 2. Добавьте боту команды приветствия
        bot.reply_to(message, 'привет, ' + message.from_user.first_name)
    elif message.text == 'играть':
        bot.reply_to(message, 'хочешь поиграть?')
    elif message.text == 'погода':                         # Задача 3. Добавьте модуль для определения погоды с помощью сайта wttr.in
        r = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, r.text)
    elif message.text == 'котик':                          # Задача 4. Перешлите с помощью бота себе файл с компьютера
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == 'файл':                           # Задача 4. Перешлите с помощью бота себе файл с компьютера
        data = open('user_message.txt', encoding='utf-8')  
        bot.send_document(message.chat.id, data)
        data.close()                
    data = open('user_message.txt', 'a+', encoding='utf-8')                   # Задача 1. Создайте telegram-бота, который записывает все ответы пользователя в файл                                                                            # записывает все ответы пользователя в файл
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как твои дела?")





    








bot.infinity_polling()