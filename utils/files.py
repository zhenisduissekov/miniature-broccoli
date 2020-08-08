#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import yaml
import logging


def load_config_yaml():
    file_path = Path('config.yaml')
    if not file_path.exists():
        logging.error('Конфигурационный файл не найден. Необходимо создать его')
        return None
    with file_path.open('r', encoding='utf-8') as stream:
        result_config = yaml.load(stream, Loader=yaml.SafeLoader)
    return result_config


def check_all_folders():
    if not os.path.exists(os.path.join('output', 'logs')):
        os.makedirs(os.path.join('output', 'logs'))


def load_user_config_yaml():
    file_path = Path('user_config.yaml')
    if not file_path.exists():
        logging.error('Конфигурационный user файл не найден. Необходимо создать его')
        return None
    with file_path.open('r', encoding='utf-8') as stream:
        result_config = yaml.load(stream, Loader=yaml.SafeLoader)
    return result_config


def UserURLGenerator(current_url, message_request):
    logging.info(f'UserURLGenerator {message_request}')
    config = load_config_yaml()
    url_dict = config['url_dict']
    result = current_url
    try:
        result = current_url + url_dict[message_request] + '/'
    except Exception as e:
        print(e)
        pass
    return result


def UserParamGenerator(current_dict, message_request):
    logging.info(f'UserParamGenerator {message_request}')
    config = load_config_yaml()
    params_dict = config['params_dict']
    result = current_dict
    try:
        if current_dict != '':
            result = '&' + current_dict + params_dict[message_request]
        else:
            result = current_dict + params_dict[message_request]
    except TypeError as e:
        pass
        # logging.warning(f'Error - {e}')
    return result


