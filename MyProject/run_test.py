# -*-coding:utf-8-*-

"""
@Time       :2019/2/2014:39
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :run_test.py
@Software   :PyCharm
@Function   :
"""

import unittest
from libext import HTMLTestRunnerNew
from common import contants

discover = unittest.defaultTestLoader.discover(contants.testcases_dir, pattern="test_*.py", top_level_dir=None)

with open(contants.reports_html, "wb+")as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='xp')
    runner.run(discover)  # 执行查找到的用例
