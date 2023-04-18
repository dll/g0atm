import unittest
from unittest.mock import Mock
import login_atm_mysql

class Test_login_app(unittest.TestCase):
    def setUp(self):
        login_atm_mysql.inputusername = Mock()
        login_atm_mysql.inputusername.return_value = "atm"
        login_atm_mysql.inputpin = Mock()
        login_atm_mysql.inputpin.return_value = "gitops123"

    def test_createconnection(self):
        self.assertIsNotNone(login_atm_mysql.createconnection())

    def test_islogin(self):
        is_forbidden, login_time = login_atm_mysql.islogin(True, "atm")
        self.assertEqual(is_forbidden, 0)
