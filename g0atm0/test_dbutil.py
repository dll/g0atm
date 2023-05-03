import os
import unittest
from unittest.mock import Mock
from customer import Customer
from dbutil import DbUtil
from pgini import  PgIni


class TestDbUtil(unittest.TestCase):

    dbutil=None
    def setUp(self):
        self.dbutil = DbUtil()

    def test_create_connection(self):
        pgini = PgIni()
        self.assertIsNotNone(self.dbutil.create_connection(), "测试数据库链接，OK")

    def test_validate_id_true(self):
        Customer.input_id = Mock()
        Customer.input_id.return_value = "123456"
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "123456"
        self.assertEqual(self.dbutil.validate_id(self.dbutil.create_connection(), Customer.input_id.return_value), True, "账号匹配")
    def test_validate_id_pin(self):
        Customer.input_id = Mock()
        Customer.input_id.return_value = "111111"
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "222222"
        self.assertEqual(self.dbutil.validate_id(self.dbutil.create_connection(), Customer.input_id.return_value), True, "账号匹配")

    def test_validate_id_false(self):
        Customer.input_id = Mock()
        Customer.input_id.return_value = "123457"
        self.assertEqual(self.dbutil.validate_id(self.dbutil.create_connection(), Customer.input_id.return_value), False, "账号错误")

    def test_validate_id_less6(self):
        Customer.input_id = Mock()
        Customer.input_id.return_value = "12345"
        self.assertEqual(self.dbutil.validate_id(self.dbutil.create_connection(), Customer.input_id.return_value), False,
                         "账号小于6位数字")

    def test_validate_id_more6(self):
        Customer.input_id = Mock()
        Customer.input_id.return_value = "1234567"
        self.assertEqual(self.dbutil.validate_id(self.dbutil.create_connection(), Customer.input_id.return_value), False,
                         "账号大于6位数字")

    def test_validate_pin_true(self):
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "123456"
        cpin = "123456";
        self.assertEqual(self.dbutil.validate_pin(cpin, DbUtil.input_pin.return_value), True, "密码匹配")

    def test_validate_pin_false(self):
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "123456"
        cpin = "222222";
        self.assertEqual(self.dbutil.validate_pin(cpin, DbUtil.input_pin.return_value), False, "密码错误")

    def test_validate_pin_less6(self):
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "23456"
        cpin = "222222";
        self.assertEqual(self.dbutil.validate_pin(cpin, DbUtil.input_pin.return_value), False, "密码小于6位数字")

    def test_validate_pin_more6(self):
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "1234567"
        cpin = "222222";
        self.assertEqual(self.dbutil.validate_pin(cpin, DbUtil.input_pin.return_value), False, "密码大于6位数字")