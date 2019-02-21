# -*-coding:utf-8-*-

"""
@Time       :2019/2/2010:56
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :logger.py
@Software   :PyCharm
@Function   :
"""

import logging
import logging.handlers
from common import contants
from common.config import ReadConfig

config = ReadConfig()
logger_level = config.get('log', 'logger_level')
file_handler_level = config.get('log', 'file_handler_level')
console_handler_level = config.get('log', 'console_handler_level')


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # 定义输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)

    file_handler = logging.handlers.RotatingFileHandler(contants.case_log, maxBytes=20 * 1024 * 1024, backupCount=10,
                                                        encoding='utf-8')
    file_handler.setLevel(file_handler_level)
    file_handler.setFormatter(formate)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_handler_level)
    console_handler.setFormatter(formate)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
