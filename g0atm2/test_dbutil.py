import unittest
from unittest.mock import Mock
from Customer import Customer
from DbUtil import DbUtil


class Test_DbUtil(unittest.TestCase):
    dbutil = DbUtil(dbname='atm', user='dll', password='gitops123', host='localhost', port='5432');

    def test_createConnection(self):
        self.assertIsNotNone(self.dbutil.createConnection(), "测试数据库链接，OK")

    def test_validateID_True(self):
        Customer.inputId = Mock()
        Customer.inputId.return_value = "123456"
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(), Customer.inputId.return_value, None), 1, "账号匹配")

    def test_validateID_False(self):
        Customer.inputId = Mock()
        Customer.inputId.return_value = "123457"
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(), Customer.inputId.return_value, None), 0, "账号错误")

    def test_validatePIN_True(self):
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "123456"
        cpin = "123456";
        self.assertEqual(self.dbutil.validatePIN(cpin, DbUtil.inputPin.return_value), 1, "密码匹配")

    def test_validatePIN_False(self):
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "123456"
        cpin = "222222";
        self.assertEqual(self.dbutil.validatePIN(cpin, DbUtil.inputPin.return_value), 0, "密码错误")
