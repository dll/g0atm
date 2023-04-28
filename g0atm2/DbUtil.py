#######################################################
# 
# DbUtil.py
# Python implementation of the Class DbUtil
# Generated by Enterprise Architect
# Created on:      27-4月-2023 19:55:34
# Original author: The Administrator
# 
#######################################################
import psycopg2.extras


# 数据库实用程序：连接数据库，减少存取转查等连接数据库的重复代码。复用此类
class DbUtil:
    __dbname = 'atm'
    __host = 'localhost'
    __password = 'gitops123'
    __port = '5432'
    __user = 'dll'

    def __init__(self, dbname, host, password, port, user):
        self.dbname = dbname
        self.host = host
        self.password = password
        self.port = port
        self.user = user

    # 创建应用与数据库之间的连接
    def createConnection(self):
        connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host,
                                      port=self.port)
        return connection

    # 验证顾客账号和密码，先验证账号，再通过调用validatePIN函数验证密码
    def validateID(self, connection, id, pin):
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
                print("无此顾客账号存在！")
                return False;
            # 从PG数据库atm中获取顾客信息
            cid = item["cid"];
            cpin = item["cpin"];
            # 验证密码是否正确
            pin=input("请输入密码：");
            isLogin = self.validatePIN(pin, cpin);
            if isLogin:
                return True;
            else:
                return False;

    # 验证顾客密码的正确性
    def validatePIN(self, cpin, pin):
        if pin != cpin:
            return False;
        else:
            return True;