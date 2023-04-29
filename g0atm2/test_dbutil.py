import unittest
from unittest.mock import Mock
import psycopg2.extras
from Customer import Customer
from DbUtil import DbUtil

class Test_DbUtil(unittest.TestCase):
    dbutil = DbUtil(dbname='atm', user='dll', password='gitops123', host='localhost', port='5432');
    def setUp(self):
        Customer.inputId = Mock()
        Customer.inputId.return_value = "123456"
        DbUtil.inputPin = Mock()
        DbUtil.inputPin.return_value = "123456"

    def test_createConnection(self):
        self.assertIsNotNone(self.dbutil.createConnection(),"测试数据库链接，OK")

    def test_validateID_True(self):
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(),"111111",None), 0, "账号匹配")
    def test_validateID_False(self):
        self.assertEqual(self.dbutil.validateID(self.dbutil.createConnection(),"111112",None), 0, "账号匹配")
    def test_validatePIN_True(self):
        cpin="123456";
        pin="123456";
        self.assertEqual(self.dbutil.validatePIN(cpin,pin), 1, "密码匹配")
    def test_validatePIN_False(self):
        cpin="111111";
        pin="123456";
        self.assertEqual(self.dbutil.validatePIN(cpin,pin), 0, "密码不一致")