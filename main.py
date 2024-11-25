#!/usr/bin/env python
from telebot import TeleBot, types
import logging
import pprint
from pathlib import Path
import os


# Настройки проекта
TOKEN = ''
DEBUG = True  # Включить логирование

# Определяем пути до базовой директории проекта и директории с медиафайлами
BASE_DIR = Path(__file__).resolve().parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files')


# Создаем объект бота и передаём ему токен регистрации в телеграмм.
bot = TeleBot(TOKEN)


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

    # Сохраняем имя пользователя в переменную.
    user_name = message.from_user.first_name

    # Подготавливаем сообщение
    # текст
    message_text = (
        f'Привет, {user_name}! \n'
        f'Здесь ты узнаешь истории выпускников лицея 1580'
    ),
    # Картинка
    photo_path = os.path.join(MEDIA_ROOT, 'shcool_1580_logo.png')
    with open(photo_path, 'rb') as photo:

        # Подготавливаем копки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("О проекте")
        item2 = types.KeyboardButton("Наши выпускники")
        markup.add(item1, item2)

        # Отправляем фото с текстом и кнопками
        bot.send_photo(
            message.chat.id,
            photo=photo,
            caption=message_text,
            reply_markup=markup
        )

# @bot.message_handler()


# Вызываем бота. Он запускается и ждёт команду.
bot.infinity_polling()
