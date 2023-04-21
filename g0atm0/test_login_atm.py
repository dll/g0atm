import unittest
from unittest.mock import Mock
import login_atm


class Test_login_app(unittest.TestCase):
    def setUp(self):
        login_atm.inputCustomerName = Mock()
        login_atm.inputCustomerName.return_value = "206004"
        login_atm.inputCustomerPin = Mock()
        login_atm.inputCustomerPin.return_value = "102419"

    def test_createConnection(self):
        self.assertIsNotNone(login_atm.createConnection(),"测试数据库链接，OK")

    def test_isLogin1(self):
        is_forbidden, login_time = login_atm.isLogin(True, "123456")
        self.assertEqual(is_forbidden, 0, "测试123456账号登录，OK")
    def test_isLogin2(self):
        is_forbidden, login_time = login_atm.isLogin(True, "206004")
        self.assertEqual(is_forbidden, 0, "测试206004账号登录，OK")
    def test_isLogin3(self):
        login_atm.inputCustomerPin.return_value = "111111"
        is_forbidden, login_time = login_atm.isLogin(False, "111111")
        self.assertEqual(is_forbidden, 1, "测试111111账号登录，NO")