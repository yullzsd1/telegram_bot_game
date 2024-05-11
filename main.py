import random

import telebot

API_TOKEN = '6520120722:AAFz6AyzcfggJI2P3fMh5i1NHUKCimNZMRo'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в игру 'камень ножница бумага'"
                                "выберите камень (к), ножницы (н) или бумагу (б)" )


@bot.message_handler(func=lambda message: True)
def play_game(message):
    text = message.text
    if text not in ['k', 'н', 'б']:
        bot.reply_to(message, "пожалуйста введите либо к, н или б")
    else:
      computer_move  =random.choice(["к", "н" "б"])

bot.infinity_polling()