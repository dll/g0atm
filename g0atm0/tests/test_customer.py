# -*- coding: UTF-8 -*-
import unittest
from unittest.mock import Mock

class TestCustomer(unittest.TestCase):
    def test_login_true(self):
        from g0atm0.views.customer import Customer
        from g0atm0.models.dbutil import DbUtil
        customer = Customer()
        Customer.input_id = Mock()
        Customer.input_id.return_value = "111111"
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "222222"
        self.assertEqual(customer.login(), True, "账号密码匹配，登录ATM成功")

    def test_login_false(self):
        from g0atm0.views.customer import Customer
        from g0atm0.models.dbutil import DbUtil
        customer = Customer()
        Customer.input_id = Mock()
        Customer.input_id.return_value = "123456"
        DbUtil.input_pin = Mock()
        DbUtil.input_pin.return_value = "111111"
        self.assertEqual(customer.login(), False, "账号或密码错误，登录ATM失败")
