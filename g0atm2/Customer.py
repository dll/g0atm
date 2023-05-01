#######################################################
# 
# Customer.py
# Python implementation of the Class Customer
# Generated by Enterprise Architect
# Created on:      27-4月-2023 20:06:55
# Original author: dll
# 
#######################################################
from DbUtil import DbUtil

class Customer:
    __id = '123456'
    __pin = '123456'

    def input_id(self):
        # id = input("请输入账号：");
        id = "123456"
        return id;

    # 顾客通过账号、密码登录ATM系统
    def login(self):
        # id=input("请输入账号：");
        id = self.input_id();
        # pin=input("请输入密码：");
        try:
            # 调用DbUtil的createConnection方法创建连接对象connection，并返回connection
            dbutil = DbUtil(dbname='atm', user='dll', password='gitops123', host='localhost', port='5432');
            connection = dbutil.create_connection();
            # 根据连接实用工具类dbutil的方法validateID，返回不同登录结果
            if dbutil.validate_id(connection, id):
                print("登录成功！欢迎 %s，使用ATM！"% id);
                return True;
            else:
                print("登录失败！账号或密码错误！");
                return False;
        finally:
            # 关闭连接(良好编程习惯)
            connection.close();

c = Customer();
c.login();