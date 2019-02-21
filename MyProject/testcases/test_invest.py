# -*-coding:utf-8-*-

"""
@Time       :2019/2/1920:34
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :test_invest.py
@Software   :PyCharm
@Function   :
"""

import unittest
from common.do_excel import DoExcel
from common.request import Request
from common import contants
from libext.ddt_new import ddt, data
from common import context
from common.mysql import MysqlUtil
from common.context import Context
from common import logger

logger = logger.get_logger('case')


@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('invest')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):
        pass

    @data(*cases)
    def test_invest(self, case):
        logger.info("开始执行第{}条用例".format(case.id))

        # 查找参数化的测试数据，动态替换
        data_new = context.replace(case.data)

        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_new)

        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(case.expected, resp.json()['code'], "login error")

            # 一致就写入Excel的结果为pass，并且
            self.do_excel.write_result('invest', case.id + 1, resp.text, 'PASS')
            logger.info("第{}条用例执行结果:PASS".format(case.id))

            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select Id from future.loan where memberID='{}'" \
                      " order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context, 'loan_id', str(loan_id))  # int 转成str ，后续通过正则替换

        except AssertionError as e:
            self.do_excel.write_result('invest', case.id + 1, resp.text, 'FAIL')
            logger.error("第{}条用例执行结果:FAIL".format(case.id))

            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
        cls.mysql.close()
