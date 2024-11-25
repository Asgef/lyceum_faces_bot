#!/usr/bin/env python
from telebot import TeleBot, types
import logging
from pathlib import Path
import os
import pprint  # Тот же принт, но структурирующий вывод


# Настройки проекта
TOKEN = '...'
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


# Обрабатываем команду /start и обрабатываем её
@bot.message_handler(commands=['start'])
def start(message):
    # Исследуем объект message.
    # logging.info(pprint.pformat(message.from_user.__dict__))

    # Сохраняем имя пользователя в переменную.
    user_name = message.from_user.first_name

    # Подготавливаем сообщение
    # текст
    message_text = (
        f'Привет, {user_name}! \n'
        f'Здесь ты узнаешь истории наших выпускников'
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

# Обрабатываем кнопку "О проекте"
@bot.message_handler(func=lambda message: message.text == "О проекте", content_types=['text'])
def project_info(message):
    # logging.info(message.text)
    # Подготавливаем сообщение
    # Текст. Применим Markdown
    message_text = '''
    *Проект "Вектор Выбора Пути"*

    Проект создан для того, чтобы поделиться реальными историями выпускников лицея 1580. 

    Мы собираем _вдохновляющие истории_, которые помогут нынешним и будущим лицеистам:
    - сделать осознанный выбор,
    - узнать о возможных трудностях и успехах, которые ожидают их на пути.

    Это место, где выпускники могут поделиться своим опытом, а нынешние ученики — найти *полезные советы* и поддержку.
    '''

    # Картинка
    photo_path = os.path.join(MEDIA_ROOT, 'shcool_1580_baner.webp')
    with open(photo_path, 'rb') as photo:

        bot.send_photo(
            message.chat.id,
            photo=photo,
            caption=message_text,
            parse_mode="Markdown"
        )


# Обрабатываем кнопку "Наши выпускники"
@bot.message_handler(func=lambda message: message.text == "Наши выпускники", content_types=['text'])
def graduates(message):
    logging.info(message.text)
    message_text = '''
        Наши выпускники поступают в ведущие учебные заведения страны.
        Узнай их истории.
    '''
    # Подготавливаем инлайн кнопки
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Все выпускники", callback_data="all_graduates")
    item2 = types.InlineKeyboardButton("2022", callback_data="2022")
    item3 = types.InlineKeyboardButton("2021", callback_data="2021")
    item4 = types.InlineKeyboardButton("2020", callback_data="2020")
    item5 = types.InlineKeyboardButton("2019", callback_data="2019")
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(
        message.chat.id,
        message_text,
        reply_markup=markup
    )


# Вызываем бота. Он запускается и ждёт команду.
bot.infinity_polling()
