# -*-coding:utf-8-*-

"""
@Time       :2019/2/1814:19
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :request.py
@Software   :PyCharm
@Function   :
"""

import requests
from common.config import ReadConfig
from common import logger

logger = logger.get_logger('request')


class Request:

    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session

    def request(self, method, url, data=None):
        method = method.upper()  # 将字符转成全部大写

        config = ReadConfig()
        pre_url = config.get('api', 'pre_url')
        url = pre_url + url

        if data is not None and type(data) == str:
            data = eval(data)  # 如果是字符串就转成字典

        logger.info('method:{0}   url:{1}'.format(method, url))
        logger.info('data:{}'.format(data))

        if method == 'GET':
            resp = self.session.request(method, url=url, params=data)
            logger.info('response:{}'.format(resp.text))
            return resp

        elif method == 'POST':
            resp = self.session.request(method, url=url, data=data)
            logger.info('response:{}'.format(resp.text))
            return resp

        else:
            logger.error('Un-support method!!!')
