#!/usr/bin/python3
# -*- coding: utf-8 -*-


from db import MysqlDB
from utils.files import load_config_yaml, UserURLGenerator, UserParamGenerator
from utils.resources import KrishaWeb
import telebot
from my_logger import LoggerConfigWithOutput
from utils.files import CheckAllFolders, ResetGlobalBariables, CommandToLink

config = load_config_yaml()
bot = telebot.TeleBot(config['TOKEN'])
user_request_url = 'https://krisha.kz/'
user_request_params = {'page': 1}
current_state = -1
current_advert = 1
current_advert_total = 1
krisha_ads = None


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
    global user_request_url, user_request_params, current_state, current_advert, krisha_ads, current_advert_total
    markup = telebot.types.ReplyKeyboardMarkup()
    user_request_url, user_request_params = CommandToLink(user_request_url, user_request_params, message.text)
    print(user_request_url, user_request_params)
    current_state += 1
    if message.text in ['menu', 'НАЗАД К ГЛАВНОМУ МЕНЮ']:
        user_request_url = 'https://krisha.kz/'     # TODO: take these variables to function in files.py
        user_request_params = {'page': 1}
        current_state = 0
        current_advert = 1
        current_advert_total = 1
        markup.row(*config['MENU_0'][1::])
        markup.row('НАЗАД К ГЛАВНОМУ МЕНЮ')
        bot.send_message(message.chat.id, config['MENU_0'][0], reply_markup=markup)
    elif message.text in ['ПОКАЗАТЬ РЕЗУЛЬТАТ', 'ПОКАЗАТЬ ЕЩЕ']:
        markup.row('ПОКАЗАТЬ ЕЩЕ', 'НАЗАД К ГЛАВНОМУ МЕНЮ')
        if current_advert == 1:
            logging.info(f'Requesting {user_request_url}, {user_request_params}')
            krisha_ads = KrishaWeb(user_request_url, params=user_request_params)
        try:
            for i in range(current_advert, 3 + current_advert):
                print(krisha_ads.adverts[i].advert_id)
                bot.send_message(message.chat.id,
                                 str(current_advert_total) + '. https://krisha.kz' + krisha_ads.adverts[i].image,
                                 reply_markup=markup)
                current_advert = i
                current_advert_total += 1
            current_advert += 1
        except Exception as e:
            print(e)
            logging.warning(f'список закончился')
            bot.send_message(message.chat.id, 'Запросить еще объявления?', reply_markup=markup)
            current_advert = 1
            user_request_params['page'] += 1
            print(f"user_request_params[page] = {user_request_params['page']}")
            krisha_ads = KrishaWeb(user_request_url, params=user_request_params)
    else:
        try:
            markup.row(*config['MENU_' + str(current_state)][1:4])
            markup.row(*config['MENU_' + str(current_state)][5:8])
            markup.row(*config['MENU_' + str(current_state)][8:10])
            bot.send_message(message.chat.id, config['MENU_' + str(current_state)][0], reply_markup=markup)
        except KeyError:
            logging.warning(f'Нет такого MENU_{current_state}')
            markup.row('ПОКАЗАТЬ РЕЗУЛЬТАТ', 'НАЗАД К ГЛАВНОМУ МЕНЮ')
            bot.send_message(message.chat.id, 'ВАШ ЗАПРОС СФОРМИРОВАН', reply_markup=markup)


if __name__ == '__main__':
    CheckAllFolders()
    logging = LoggerConfigWithOutput()
    logging.info('Телеграм бот запущен')
    bot.polling(none_stop=True)

    # krisha_ads = KrishaWeb()
    # print(krisha_ads.adverts)
    # config = load_config_yaml()
    # my_db = MysqlDB(config)
    # my_db.SaveToMySQL(krisha_ads)
