import telebot
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Kilo Claw Automation Activa. Esperando archivos Cube ACR...')

if __name__ == '__main__':
    bot.polling()
