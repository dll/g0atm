import unittest
from unittest.mock import Mock
import psycopg2.extras
from Customer import Customer
from DbUtil import DbUtil


class Test_Customer(unittest.TestCase):
    def test_login_True(self):
        customer = Customer()
        Customer.inputId = Mock()
        Customer.inputId.return_value = "123456"
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "123456"
        self.assertEqual(customer.login(), True, "账号密码匹配，登录ATM成功")

    def test_login_False(self):
        customer = Customer()
        Customer.inputId = Mock()
        Customer.inputId.return_value = "123456"
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "111111"
        self.assertEqual(customer.login(), False, "账号或密码错误，登录ATM失败")
