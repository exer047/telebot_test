import telebot
import parser_lh

bot = telebot.TeleBot("***************************************")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to my testbot!")


@bot.message_handler(commands=['random'])
def send_news(message):
    bot.reply_to(message, parser_lh.return_random_link(parser_lh.link_list))


@bot.message_handler(content_types="sticker")
def send_answer(message):
    bot.send_message(message.chat.id, text="Thanks for your sticker!")


@bot.message_handler(regexp='help')
def command_help(message):
    bot.send_message(message.chat.id, 'Did someone call for help?')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
