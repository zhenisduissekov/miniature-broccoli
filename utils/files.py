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


def CheckAllFolders():
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
        if url_dict[message_request] not in current_url:
            result = current_url + url_dict[message_request] + '/'
    except Exception as e:
        print(e)
        pass
    return result


def UserParamGenerator(current_dict, message_request):
    logging.info(f'UserParamGenerator {message_request}')
    config = load_config_yaml()
    params_dict = config['params_dict']
    try:
        current_dict[params_dict[message_request]] = ''
    except:
        pass
        # logging.warning(f'Error - {e}')
    return current_dict


def ResetGlobalBariables():
    pass
    # FIXME: take out all of the variables needed to be reset
    # global user_request_url, user_request_params, current_state, current_advert, krisha_ads


def CommandToLink(ctl_user_request_url, ctl_user_request_params, ctl_message):
    ctl_user_request_url = UserURLGenerator(current_url=ctl_user_request_url, message_request=ctl_message)
    ctl_user_request_params = UserParamGenerator(current_dict=ctl_user_request_params, message_request=ctl_message)
    return ctl_user_request_url, ctl_user_request_params
