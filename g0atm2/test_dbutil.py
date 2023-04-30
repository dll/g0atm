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

    def test_validateID_Less6(self):
        Customer.inputId = Mock()
        Customer.inputId.return_value = "12345"
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(), Customer.inputId.return_value, None), 0,
                         "账号小于6位数字")

    def test_validateID_More6(self):
        Customer.inputId = Mock()
        Customer.inputId.return_value = "1234567"
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(), Customer.inputId.return_value, None), 0,
                         "账号大于6位数字")

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

    def test_validatePIN_Less6(self):
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "23456"
        cpin = "222222";
        self.assertEqual(self.dbutil.validatePIN(cpin, DbUtil.inputPin.return_value), 0, "密码小于6位数字")

    def test_validatePIN_More6(self):
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "1234567"
        cpin = "222222";
        self.assertEqual(self.dbutil.validatePIN(cpin, DbUtil.inputPin.return_value), 0, "密码大于6位数字")