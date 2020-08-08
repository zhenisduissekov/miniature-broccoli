#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from pymysql.cursors import DictCursor
import sys
import logging


class MysqlDB:
    def __init__(self, config):
        self.host = config['HOST']
        self.username = config['USER']
        self.password = config['PASSWORD']
        self.db = config['DB']
        self.charset = config['CHARSET']
        self.connection = None

    def open_connection(self):
        try:
            if self.connection is None:
                self.connection = pymysql.connect(
                    self.host,
                    user=self.username,
                    passwd=self.password,
                    db=self.db,
                    charset=self.charset,
                    connect_timeout=5
                )
        except pymysql.MySQLError as e:
            logging.error(e)
            sys.exit()

    def run_query(self, query):
        try:
            self.open_connection()
            with self.connection.cursor() as cursor:
                if 'SELECT' in query:
                    records = []
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for row in result:
                        records.append(row)
                    cursor.close()
                    return records
                else:
                    cursor.execute(query)
                    self.connection.commit()
                    cursor.close()

        except pymysql.MySQLError as e:
            logging.error(f'{e}')
        finally:
            if self.connection:
                self.connection.close()
                self.connection = None
                logging.info('Database connection closed')

    def SaveToMySQL(self, data_to_db):
        try:
            self.run_query("DROP TABLE KRISHA_ADS")
        except Exception as e:
            print('No table found')

        self.run_query(f"""CREATE TABLE KRISHA_ADS (
                                    ad_id INT, 
                                    advert_id VARCHAR(20), 
                                    title VARCHAR(100), 
                                    price VARCHAR(50), 
                                    text VARCHAR(400),
                                    image VARCHAR(100), 
                                          PRIMARY KEY(ad_id)
                                    ) 
                                    CHARACTER SET utf8;"""
                       )

        for i in range(1, len(data_to_db.adverts)):
            self.run_query(f"""INSERT INTO KRISHA_ADS(ad_id, advert_id, title,price,text,image)
                                VALUES(
                                        {i},
                                        '{data_to_db.adverts[i].advert_id}',
                                        '{data_to_db.adverts[i].title}',
                                        '{data_to_db.adverts[i].price}',
                                        '{data_to_db.adverts[i].text}',
                                        '{data_to_db.adverts[i].image}'
                                        );"""
                           )
