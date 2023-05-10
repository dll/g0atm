# -*- coding: UTF-8 -*-

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest

# 加载测试用例
from g0atm0.tests import test_customer
import test_dbutil

class TestIntergrate:

    def test_login_atm(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录成功
        suite.addTest(test_dbutil.TestDbUtil("test_create_connection"))
        suite.addTest(test_dbutil.TestDbUtil("test_validate_id_true"))
        suite.addTest(test_dbutil.TestDbUtil("test_validate_pin_true"))
        suite.addTest(test_customer.TestCustomer("test_login_true"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    def test_login_atm_id_fail(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录失败：账号错误
        suite.addTest(test_dbutil.TestDbUtil("test_create_connection"))
        suite.addTest(test_dbutil.TestDbUtil("test_validate_id_false"))
        suite.addTest(test_customer.TestCustomer("test_login_false"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    def test_login_atm_pin_fail(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录失败：密码错误
        suite.addTest(test_dbutil.TestDbUtil("test_create_connection"))
        suite.addTest(test_dbutil.TestDbUtil("test_validate_id_true"))
        suite.addTest(test_dbutil.TestDbUtil("test_validate_pin_false"))
        suite.addTest(test_customer.TestCustomer("test_login_false"))

    # 运行测试用例
        runner = unittest.TextTestRunner()
        runner.run(suite)

itest = TestIntergrate()
itest.test_login_atm()
itest.test_login_atm_id_fail()
itest.test_login_atm_pin_fail()