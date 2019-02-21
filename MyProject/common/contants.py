# -*-coding:utf-8-*-

"""
@Time       :2019/2/1814:08
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :contants.py
@Software   :PyCharm
@Function   :常量
"""

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_dir = os.path.join(base_dir, "datas")  # 测试数据的文件夹
conf_dir = os.path.join(base_dir, "conf")  # 配置文件的文件夹
logger_dir = os.path.join(base_dir, 'logs')

case_file = os.path.join(data_dir, "cases.xlsx")

test_conf = os.path.join(conf_dir, "test.conf")
test2_conf = os.path.join(conf_dir, "test2.conf")
global_conf = os.path.join(conf_dir, "global.conf")

case_log = os.path.join(logger_dir, 'case.log')

testcases_dir = os.path.join(base_dir, 'testcases')

reports_dir = os.path.join(base_dir, 'reports')
reports_html = os.path.join(reports_dir, 'reports.html')
