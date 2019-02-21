# -*-coding:utf-8-*-

"""
@Time       :2019/2/1910:14
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :mysql.py
@Software   :PyCharm
@Function   :
"""

import pymysql
from common.config import ReadConfig


class MysqlUtil:

    def __init__(self, return_dict = False):

        config = ReadConfig()

        host = config.get('db', 'host')
        user = config.get('db', 'user')
        password = config.get('db', 'password')
        port = config.getint('db', 'port')

        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)

        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)
        else:
            self.cursor = self.mysql.cursor()

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.cursor.close()
        self.mysql.close()
