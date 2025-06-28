import telebot
from config import token
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot(token)
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
# Запуск бота
bot.polling()
