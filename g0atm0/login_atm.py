'''
(1) 顾客输入顾客账号，如不存在此顾客不能登录；
(2) 顾客在输入密码时，如果连续输入三次错误，则该顾客被锁定一段时间;
(3) 顾客被锁定一段时间后，可再次进行尝试登录；
'''
import psycopg2.extras
import datetime

'''
pip3 install pymysql -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
'''


def isForbidden(cisforbidden, clogintime):
    is_login = False
    # 判断顾客是否被禁
    if cisforbidden:
        last_login_time = clogintime
        login_time = datetime.datetime.now()
        waiting_time = int(((login_time - last_login_time).total_seconds()) / 60)
        # 顾客如果被禁，判断还需要多长时间等待
        if (waiting_time - 3) < 0:
            print("账号暂时锁定，请等待%d分钟" % (3 - waiting_time))
            # break
            exit()


def inputCustomerPin():
    #return input("请输入密码：");
    return "102419"


def is3times_validate_pin(cpin):
    times = 0
    is_login = False
    # 3次输入密码的机会
    while times < 3:
        # password = input("请输入密码：")
        # password = "gitops123"
        password = inputCustomerPin();
        if password != cpin:
            times += 1
        else:
            is_login = True
            break
    return is_login


def isLogin(is_login, customerName):
    # 登录成功与否，禁用信息以及登录信息数据都在数据库进行更新
    if is_login:
        is_forbidden = 0
        # 将datetime转换字符串类型
        login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("欢迎%s，登陆成功！" % (customerName))
    else:
        is_forbidden = 1
        login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("登录失败，请等待3分钟")
    return is_forbidden, login_time


def validate_username(connection, customerName):
    with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # 根据顾客名查出顾客信息
        sql = "select name, pin, is_forbidden, login_time from customer where name='%s';" % customerName
        cursor.execute(sql)
        item = cursor.fetchone()
        # 判断是否存在此顾客
        #if 0 == result:
        if item is None:
            print("无此顾客名存在！")
            return False;
            # continue
            #loginatmcui(connection)

        # 获取顾客信息
        #item = cursor.fetchone()
        cname=item["name"];
        cpin=item["pin"];
        cisforbidden=item["is_forbidden"];
        clogintime=item["login_time"];
        # 判断是否被禁用
        isForbidden(cisforbidden, clogintime);
        # 判断是否超过3次输入密码
        is_login = is3times_validate_pin(cpin);
        # 判断是否登录成功
        is_forbidden, login_time = isLogin(is_login, customerName);

        # 更新数据库的Mysql语句
        sql = "update customer set is_forbidden = %d , login_time = '%s' where name='%s'" % (
            is_forbidden, login_time, customerName)
        cursor.execute(sql)

        # 由于对数据库进行了更新，故需要提交事务
        connection.commit()
        # break
    return True;

def inputCustomerName():
    #return input("输入顾客名：")
    return "206004"

def loginAtmCui(connection):
    while True:
        # customerName = input("输入顾客名：")
        # customerName = "atm"
        customerName = inputCustomerName()
        if "q" != customerName and "Q" != customerName:
            if len(customerName) != 6:
                print("退出，顾客账号长度6位数字！！！");
            else:
                if validate_username(connection, customerName):
                    break;
        else:
            print("q\Q用户退出！！！");
            break


def createConnection():
    # 创建数据库的链接
    connection = psycopg2.connect(database='atm', user='dll', password='gitops123', host='localhost', port='5432')
    return connection


def loginApp():
    try:
        connection = createConnection();
        loginAtmCui(connection);
    finally:
        # 最终关闭链接
        connection.close();


loginApp()
