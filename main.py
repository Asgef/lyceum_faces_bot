#!/usr/bin/env python
from telebot import TeleBot, types

import logging # Для логирования, выводит в консоль необходимые сообщения, помогает в отладке.

from pathlib import Path
import os  # Помогает сформировать пути до файлов
import pprint  # Тот же принт, но структурирующий вывод
# Данные из базы данных
from db import universities, questions,question_order # Имитируем базу данных
import time  # Для задержки между отправкой сообщений


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


# Обрабатываем команду /start
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
    logging.info(message.text)
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

        # Отправляем
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

    # Подготавливаем инлайн-кнопки университетов.
    # Для каждого университета создаем инлайн-кнопку в цикле.
    markup = types.InlineKeyboardMarkup(row_width=1)
    for uni_key, uni_info in universities.items():
        button = types.InlineKeyboardButton(
            uni_info['name'],
            callback_data=f'university_{uni_key}'
        )
        markup.add(button)

    # Отправляем
    bot.send_message(
        message.chat.id,
        message_text,
        reply_markup=markup
    )


# Обрабатываем инлайн кнопки для университета
@bot.callback_query_handler(func=lambda call: call.data.startswith('university_'))
def handle_university_selection(call):
    # Извлекаем ключ университета
    university_key = call.data[len('university_'):]
    university = universities[university_key]
    graduates = university['graduates']

    # Создаем инлайн-кнопки для выпускников
    markup = types.InlineKeyboardMarkup(row_width=1)
    for grad_key, grad_info in graduates.items():
        button = types.InlineKeyboardButton(
            grad_info['name'],
            callback_data=f'graduate_{university_key}_{grad_key}'
        )
        markup.add(button)

    # Путь к фотографии университета
    photo_path = os.path.join(MEDIA_ROOT, university['photo'])

    # Отправляем фотографию университета и кнопки выпускников
    with open(photo_path, 'rb') as photo: # Загружаем файл в контекстном менеджере

        # Отправляем
        bot.send_photo(
            call.message.chat.id,
            photo=photo,
            caption=f"Выпускники из {university['name']}:",
            reply_markup=markup
        )

# Обрабатываем инлайн кнопки для выпускника
@bot.callback_query_handler(func=lambda call: call.data.startswith('graduate_'))
def handle_graduate_selection(call):
    # Извлекаем ключи университета и выпускника
    _, university_key, graduate_key = call.data.split('_', 2)
    graduate = universities[university_key]['graduates'][graduate_key]

    # Сообщение получается слишком длиным, телеграм ругается, поэтому делим его на части
    # Разбиваем вопросы-ответы на три части
    parts = [
        question_order[:5],  # Первые 5 вопросов
        question_order[5:10],  # С 6 по 10 вопрос
        question_order[10:]  # С 11 по 16 вопрос
    ]

    # Отправляем первое сообщение с фото и короткой подписью
    photo_path = os.path.join(MEDIA_ROOT, graduate['photo'])
    with open(photo_path, 'rb') as photo:
        bot.send_photo(
            call.message.chat.id,
            photo=photo,
            caption=f"*Имя:* {graduate['name']}",
            parse_mode="Markdown"
        )

    # Небольшая задержка перед отправкой текстовых сообщений
    time.sleep(2)

    # Отправляем три текстовых сообщения с вопросами-ответами
    for part in parts:
        message_text = ""
        for q_id in part:
            question = questions[q_id]
            answer = graduate['answers'][q_id]
            message_text += f"*Вопрос:* {question}\n*Ответ:* {answer}\n\n"
        bot.send_message(
            call.message.chat.id,
            message_text,
            parse_mode="Markdown"
        )
        time.sleep(3)  # Задержка между сообщениями


# Вызываем бота. Он запускается и ждёт команду.


# Может произойти ошибка, бот остановится и не запустится.
# Для этого запускаем бота в бесконечном цикле в блоке try_except.
# Если бот упал, то он перезапустится через 5 секунд
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        time.sleep(5)  # Задержка перед перезапуском
