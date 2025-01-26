import telebot
from dictionary import yakut_dict

# Вставьте сюда ваш токен от BotFather
bot = telebot.TeleBot("8156964592:AAEc7QwSoAw3bp4rnL-k05PMvZeTy4j0eew")

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот-словарь якутского языка. Напиши слово, и я найду его значение.')

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text.lower()  # Приводим к нижнему регистру
    if user_message in yakut_dict:
        response = f"{user_message}: {yakut_dict[user_message]}"
    else:
        response = f"Извините, слово '{user_message}' не найдено в словаре."
    bot.reply_to(message, response)

# Запуск бота
bot.polling()