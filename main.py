#!/usr/bin/env python
from multiprocessing.util import DEBUG

import telebot
import logging
import pprint


# Настройки проекта
TOKEN = ''
DEBUG = True  # Включить логирование


# Создаем объект бота и передаём ему токен регистрации в телеграмм.
bot = telebot.TeleBot(TOKEN)


# Настройки логирования. Для отладки и исследования.
if DEBUG:
    logging.basicConfig(
        level=logging.INFO,  # Устанавливаем уровень логирования
        format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщений
        datefmt="%Y-%m-%d %H:%M:%S"  # Формат даты
    )


# Перехватываем команду /start и обрабатываем её
@bot.message_handler(commands=['start'])
def start(message):
    # Исследуем объект message.
    logging.info(pprint.pformat(message.from_user.__dict__))

    # Сохраняем имя пользователя в переменную и отвечаем ему.
    user_name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f'Привет, {user_name}! \n'
        f'Здесь ты узнаешь истории выпускников лицея 1580'
    )


# Вызываем бота. Он запускается и ждёт команду.
bot.infinity_polling()
