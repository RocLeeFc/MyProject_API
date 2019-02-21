# -*-coding:utf-8-*-

"""
@Time       :2019/2/1910:26
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :test_register.py
@Software   :PyCharm
@Function   :
"""
import unittest
import json
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from libext.ddt_new import ddt, data
from common.mysql import MysqlUtil
from common import logger

logger = logger.get_logger('case')


@ddt
class RegisterTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('register')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 实例化对象

    def setUp(self):
        self.mysql = MysqlUtil(return_dict=True)
        sql = "select max(mobilephone) as max_phone from future.member"
        self.max = self.mysql.fetch_one(sql)['max_phone']

    @data(*cases)
    def test_register(self, case):
        logger.info("开始执行第{}条用例".format(case.id))

        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == "${register_mobile}":
            data_dict['mobilephone'] = int(self.max) + 1

        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_dict)

        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "login error")

            if resp.json()['msg'] == '注册成功':
                sql = 'select * from future.member where mobilephone = {}'.format(data_dict['mobilephone'])
                results = self.mysql.fetch_all(sql)

                self.assertEqual(1, len(results))
                member = results[0]
                self.assertEqual(0, member['LeaveAmount'])

            # 一致就写入Excel的结果为pass，并且
            self.do_excel.write_result('register', case.id + 1, resp.text, 'PASS')

            logger.info("第{}条用例执行结果:PASS".format(case.id))

        except AssertionError as e:
            self.do_excel.write_result('register', case.id + 1, resp.text, 'FAIL')

            logger.error("第{}条用例执行结果:FAIL".format(case.id))

            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
