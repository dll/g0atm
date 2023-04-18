import unittest
from unittest.mock import Mock
import g0atm0.login_atm_mysql

class Test_login_app(unittest.TestCase):
    def setUp(self):
        g0atm0.login_atm_mysql.inputusername = Mock()
        g0atm0.login_atm_mysql.inputusername.return_value = "atm"
        g0atm0.login_atm_mysql.inputpin = Mock()
        g0atm0.login_atm_mysql.inputpin.return_value = "gitops123"

    def test_createconnection(self):
        self.assertIsNotNone(g0atm0.login_atm_mysql.createconnection())

    def test_islogin(self):
        is_forbidden, login_time = g0atm0.login_atm_mysql.islogin(True, "atm")
        self.assertEqual(is_forbidden, 0)
