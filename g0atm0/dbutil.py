#######################################################
# 
# dbutil.py
# Python implementation of the Class DbUtil
# Generated by Enterprise Architect
# Created on:      27-4月-2023 19:55:34
# Original author: The Administrator
# 
#######################################################
import psycopg2.extras
from pgini import PgIni

# 数据库实用程序：连接数据库，减少存取转查等连接数据库的重复代码。复用此类

class DbUtil:

    # 创建应用与数据库之间的连接
    def create_connection(self):
        pgini = PgIni()
        connection = psycopg2.connect(dbname=pgini.get_pg_dbname(),user=pgini.get_pg_user(),password=pgini.get_pg_pwd(),
                                      host=pgini.get_pg_host(),port=pgini.get_pg_port())
        return connection

    def input_pin(self):
        pin = "123456"
        return pin

    # 验证顾客账号和密码，先验证账号，再通过调用validatePIN函数验证密码
    def validate_id(self, connection, id):
        # 由连接connection创建游标cursor
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            # 根据顾客账号查出顾客信息
            sql = "select cid, cpin from g0atm0_customer where cid='%s';" % id
            # 游标执行SQL查询
            cursor.execute(sql)
            # 获得游标中的一条记录
            item = cursor.fetchone()
            # 判断是否存在此顾客
            if item is None:
                print("账号错误！")
                return False
            # 从PG数据库atm中获取顾客信息
            cpin = item["cpin"]
            # 验证密码是否正确
            pin = self.input_pin()
            is_login = self.validate_pin(cpin, pin)
            if is_login:
                return True
            else:
                print("密码错误！")
                return False

    # 验证顾客密码的正确性
    def validate_pin(self, cpin, pin):
        if pin != cpin:
            return False
        else:
            return True
