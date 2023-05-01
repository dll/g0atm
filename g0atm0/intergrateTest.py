import unittest

# 加载测试用例
import test_customer
import test_dbutil

class TestIntergrate:

    def login_atm_itest(self):
        # 将测试用例添加到测试集合
        suite = unittest.TestSuite()
        # 测试登录成功
        suite.addTest(test_dbutil.test_dbutil("test_create_connection"))
        suite.addTest(test_dbutil.test_dbutil("test_validate_id_true"))
        suite.addTest(test_dbutil.test_dbutil("test_validate_pin_true"))
        suite.addTest(test_customer.test_customer("test_login_true"))

        # 运行测试用例
        runner = unittest.TextTestRunner()
        runner.run(suite)

itest = TestIntergrate()
itest.login_atm_itest()