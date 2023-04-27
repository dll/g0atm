#######################################################
# 
# Customer.py
# Python implementation of the Class Customer
# Generated by Enterprise Architect
# Created on:      27-4月-2023 20:06:55
# Original author: dll
# 
#######################################################
import psycopg2.extras
from DbUtil import DbUtil

class Customer:
    __id = '123456'
    __pin = '123456'
    def login(self):
        id=input("请输入账号：");
        pin=input("请输入密码：");
        dbutil = DbUtil(dbname='atm', user='dll', password='gitops123', host='localhost', port='5432');
        connection = dbutil.createConnection();
        if dbutil.validateID(connection,id,pin):
            print("欢迎 %s，使用ATM！"% id);
        else:
            print("账号或密码错误！");

c=Customer()
c.login()