'''
(1) 顾客输入顾客账号，如不存在此顾客不能登录；
(2) 顾客在输入密码时，如果连续输入三次错误，则该顾客被锁定一段时间;
(3) 顾客被锁定一段时间后，可再次进行尝试登录；
'''
import pymysql
import datetime
'''
pip3 install pymysql -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
'''
#创建数据库的链接
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='gitops123',
                             db='atm',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    while True:
        userName = input("输入顾客名：")
        if "q"!=userName and "Q"!=userName:
                with connection.cursor() as cursor:
                    #根据顾客名查出顾客信息
                    sql = 'select * from t_customer where name = %s'
                    result =  cursor.execute(sql,userName);
                    # 判断是否存在此顾客
                    if 0==result:
                        print("无此顾客名存在！")
                        continue
                    #获取顾客信息
                    item = cursor.fetchone()
                    is_login = False
                    # 判断顾客是否被禁
                    if item["is_forbidden"]:
                        last_login_time = item["login_time"]
                        login_time = datetime.datetime.now()
                        waiting_time = int(((login_time-last_login_time).total_seconds())/60)
                        #顾客如果被禁，判断还需要多长时间等待
                        if (waiting_time-3)<0:
                            print("账号暂时锁定，请等待%d分钟"%(3-waiting_time))
                            break

                    times = 0
                    # 3次输入密码的机会
                    while times<3:
                        password = input("请输入密码：")
                        if password != item["pin"]:
                            times += 1
                        else:
                            is_login = True
                            break

                    # 登录成功与否，禁用信息以及登录信息数据都在数据库进行更新
                    if is_login:
                        is_forbidden = 0
                        # 将datetime转换字符串类型
                        login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print("欢迎%s，登陆成功！"%(userName))
                    else:
                        is_forbidden = 1
                        login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print("登录失败，请等待10min")

                    # 更新数据库的Mysql语句
                    sql = "update t_customer set is_forbidden = %d , login_time = '%s' where name='%s'"%(is_forbidden,login_time,userName)
                    cursor.execute(sql)

                    # 由于对数据库进行了更新，故需要提交事务
                    connection.commit()
                    break
        else:
            print("退出！！！")
            break
finally:
    # 最终关闭链接
    connection.close();
