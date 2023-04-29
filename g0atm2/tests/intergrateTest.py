import unittest

# 加载测试用例
import test_customer
import test_dbutil

# 将测试用例添加到测试集合
suite = unittest.TestSuite()
# 测试登录成功
suite.addTest(test_dbutil.Test_DbUtil("test_createConnection"))
suite.addTest(test_dbutil.Test_DbUtil("test_validateID_True"))
suite.addTest(test_dbutil.Test_DbUtil("test_validatePIN_True"))
suite.addTest(test_customer.Test_Customer("test_login_True"))

# 运行测试用例
runner = unittest.TextTestRunner()
runner.run(suite)