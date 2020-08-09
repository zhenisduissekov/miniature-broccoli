#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import logging
import urllib

class KrishaAds:
    def __init__(self):
        self.advert_id = None
        self.image = None
        self.title = None
        self.price = None
        self.text = None

    def input(self, advert_id, image, title, text, price):
        self.advert_id = advert_id
        self.image = image
        self.title = title
        self.price = price
        self.text = text


class KrishaWeb:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.bulk = None
        self.bulk_size = 0
        self.adverts = {}
        self.max_pages = 0

        def get_max_page(gmp_soup):
            gmp_max = 0
            for i in gmp_soup.find_all("a", attrs={'data-page': re.compile(r'[\d]+')}):
                try:
                    if gmp_max < int(i.text):
                        gmp_max = int(i.text)
                except ValueError:
                    pass
            return gmp_max

        def parse_page(pp_counter, pp_soup):
            for i in soup.find_all("div", attrs={'id': re.compile(r'^id.*')}):
                pp_counter += 1
                self.adverts[pp_counter] = KrishaAds()
                advert_id = i['id']
                img = i.find('a', attrs={'class': re.compile(r'^a-card__image.*')})['href']
                text_h = " ".join((re.sub('\n', '', i.find('div', class_="a-card__header-left").text)).split())
                text_pr = " ".join((re.sub('\n', '', i.find('div', class_="a-card__price").text)).split())
                text_h_body = " ".join((re.sub('\n', '', i.find('div', class_="a-card__header-body").text)).split())
                self.adverts[pp_counter].input(advert_id=advert_id, image=img,
                                               title=text_h, price=text_pr, text=text_h_body)
            self.bulk_size = len(self.adverts)
            return pp_counter

        custom_url = url + '?page=' + str(params['page'])
        for k in params.keys():
            if k != 'page':
                custom_url += '&' + k

        request = requests.get(custom_url)
        logging.info(f'URL {request.url} [{request.status_code}]')
        if request.status_code == 200:
            html_text = request.content.decode()
            soup = BeautifulSoup(html_text, "html.parser")
            self.max_pages = get_max_page(soup)
            parse_page(0, soup)
        else:
            logging.error(f'Не правильный запрос')

