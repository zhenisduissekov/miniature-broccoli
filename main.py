#!/usr/bin/python3
# -*- coding: utf-8 -*-


from db import MysqlDB
from utils.files import load_config_yaml, UserURLGenerator, UserParamGenerator
from utils.resources import KrishaWeb
import my_logger
import telebot
from my_logger import logger_config_with_output
from utils.files import check_all_folders

config = load_config_yaml()
bot = telebot.TeleBot(config['TOKEN'])
user_request_url = 'https://krisha.kz/'
user_request_params = {}
current_state = -1


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Приветствую!\n' +
        'Для просмотра функционала бота напишите или выберете ***/menu***\n' +
        'Описание программы ***/help***',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['help', 'info'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Git', url='https://zhenisduissekov.github.io'))
    keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/zduissekov'))
    bot.send_message(
        message.chat.id,
        "Я написал этот бот в целях саморазвития.\n"
        "С его помощью я можно посмотреть какие есть объявления\n\n" 
        "Функционал пока не большой ищет по объявлениям с помошью фильтров\n\n"
        "Если заметите ошибку или есть предложения пишите мне в личку\n\n"
        "Спасибо",
        parse_mode='Markdown',
        reply_markup=keyboard
    )


@bot.message_handler(content_types='text')
def menu_command(message):
    logging.info('menu_command')
    global user_request_url, user_request_params, current_state
    user_request_url = UserURLGenerator(current_url=user_request_url, message_request=message.text)
    user_request_params = UserParamGenerator(current_dict={}, message_request=message.text)
    markup = telebot.types.ReplyKeyboardMarkup()
    current_state += 1
    if message.text in ['menu', 'НАЗАД К ГЛАВНОМУ МЕНЮ?']:
        markup.row(*config['MENU_0'][1::])
        markup.row('НАЗАД К ГЛАВНОМУ МЕНЮ?')
        user_request_url = 'https://krisha.kz/'
        user_request_params = {}
        current_state = 0
        bot.send_message(message.chat.id, config['MENU_0'][0], reply_markup=markup)
    elif message.text == 'ПОКАЗАТЬ РЕЗУЛЬТАТ?':
        logging.info('Отправляю запрос')
        markup.row('ПОКАЗАТЬ ЕЩЕ?', 'НАЗАД К ГЛАВНОМУ МЕНЮ?')
        print(f'Requesting {user_request_url}, {user_request_params}')
        krisha_ads = KrishaWeb(user_request_url)
        request = krisha_ads.adverts
        print(krisha_ads.adverts)
        for i in krisha_ads.adverts:
            print(krisha_ads.adverts[i].advert_id)
            bot.send_message(message.chat.id, str(i) + 'https://krisha.kz' + krisha_ads.adverts[i].image, reply_markup=markup)
            # if i > 5:
            #     break
    else:
        try:
            markup.row(*config['MENU_' + str(current_state)][1:4])
            markup.row(*config['MENU_' + str(current_state)][5:8])
            markup.row(*config['MENU_' + str(current_state)][8:10])
            bot.send_message(message.chat.id, config['MENU_' + str(current_state)][0], reply_markup=markup)
        except KeyError:
            logging.warning(f'Нет такого меню MENU_{current_state}')
            markup.row('ПОКАЗАТЬ РЕЗУЛЬТАТ?', 'НАЗАД К ГЛАВНОМУ МЕНЮ?')
            bot.send_message(message.chat.id, 'ВАШ ЗАПРОС СФОРМИРОВАН', reply_markup=markup)


if __name__ == '__main__':
    check_all_folders()
    logging = logger_config_with_output()
    logging.info('Телеграм бот запущен')
    bot.polling(none_stop=True)

    # krisha_ads = KrishaWeb()
    # print(krisha_ads.adverts)
    # config = load_config_yaml()
    # my_db = MysqlDB(config)
    # my_db.SaveToMySQL(krisha_ads)
