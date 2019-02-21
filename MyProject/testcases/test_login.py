# -*-coding:utf-8-*-

"""
@Time       :2019/2/1816:02
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :test_login.py
@Software   :PyCharm
@Function   :
"""

import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from libext.ddt_new import ddt, data
from common import logger

logger = logger.get_logger('case')

@ddt
class LoginTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('login')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 实例化对象

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self, case):
        logger.info("开始执行第{}条用例".format(case.id))

        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, case.data)

        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "login error")

            # 一致就写入Excel的结果为pass，并且
            self.do_excel.write_result('login', case.id + 1, resp.text, 'PASS')
            logger.info("第{}条用例执行结果:PASS".format(case.id))

        except AssertionError as e:
            self.do_excel.write_result('login', case.id + 1, resp.text, 'FAIL')
            logger.error("第{}条用例执行结果:FAIL".format(case.id))

            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
