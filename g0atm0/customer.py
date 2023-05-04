#######################################################
# 
# customer.py
# Python implementation of the Class Customer
# Generated by Enterprise Architect
# Created on:      27-4月-2023 20:06:55
# Original author: dll
# 
#######################################################

from dbutil import DbUtil

class Customer:
    id = '123456'
    pin = '123456'

    def input_id(self):
        if __debug__:
            tmp_id =  "123456"
        else:
            tmp_id=input("请输入账号：")
        return tmp_id

    # 顾客通过账号、密码登录ATM系统
    def login(self):
        tmp_id = self.input_id()
        try:
            # 调用DbUtil的createConnection方法创建连接对象connection，并返回connection
            dbutil = DbUtil()
            connection = dbutil.create_connection()
            # 根据连接实用工具类dbutil的方法validateID，返回不同登录结果
            if dbutil.validate_id(connection, tmp_id):
                self.id =tmp_id
                print("登录成功！欢迎 %s，使用ATM！"% self.id)
                return True
            else:
                print("登录失败！账号或密码错误！")
                return False
        finally:
            # 关闭连接(良好编程习惯)
            if connection:
                connection.close()
            # else:
            #    return # bug

c = Customer()
c.login()