# -*- coding: UTF-8 -*-
import unittest


class TestIntergrate:

    def test_login_atm(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录成功
        from g0atm0.tests.test_dbutil import TestDbUtil
        suite.addTest(TestDbUtil("test_create_connection"))
        suite.addTest(TestDbUtil("test_validate_id_true"))
        suite.addTest(TestDbUtil("test_validate_pin_true"))
        from g0atm0.tests.test_customer import TestCustomer
        suite.addTest(TestCustomer("test_login_true"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    def test_login_atm_id_fail(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录失败：账号错误
        from g0atm0.tests.test_dbutil import TestDbUtil
        from g0atm0.tests.test_customer import TestCustomer
        suite.addTest(TestDbUtil("test_create_connection"))
        suite.addTest(TestDbUtil("test_validate_id_false"))
        suite.addTest(TestCustomer("test_login_false"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    def test_login_atm_pin_fail(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录失败：密码错误
        from g0atm0.tests.test_dbutil import TestDbUtil
        suite.addTest(TestDbUtil("test_create_connection"))
        suite.addTest(TestDbUtil("test_validate_id_true"))
        suite.addTest(TestDbUtil("test_validate_pin_false"))
        from g0atm0.tests.test_customer import TestCustomer
        suite.addTest(TestCustomer("test_login_false"))

        # 运行测试用例
        runner = unittest.TextTestRunner()
        runner.run(suite)


itest = TestIntergrate()
itest.test_login_atm()
itest.test_login_atm_id_fail()
itest.test_login_atm_pin_fail()
