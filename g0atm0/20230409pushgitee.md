### 2023-04-09 Gitee分支与实战

#### MySQL免安装使用

根目录 >  21智能> 下载解压mysql-8.0.32-winx64.zip

mysql-8.0.32-winx64\bin目录，cmd：mysqld.exe 回车后，不关闭窗口

![image-20230409223243023](assets/image-20230409223243023.png)

mysql-8.0.32-winx64\bin目录 再开窗，cmd：mysql.exe -uroot -pgitops123

![image-20230409223303896](assets/image-20230409223303896.png)

#### PyCharm操作

pycharm get from vcs

![image-20230409223547112](assets/image-20230409223547112.png)

![image-20230409223623352](assets/image-20230409223623352.png)

也可以选择Gitee直接打开Gitee仓库（以后演示）。

#### 开发Py：LoginATM-mysql.py

![image-20230409223713331](assets/image-20230409223713331.png)

#### Git push失败及解决

pyCharm--file--setting--version control--gitee-->授权

![image-20230409222216177](assets/image-20230409222216177.png)

![image-20230409222114899](assets/image-20230409222114899.png)

![image-20230409221111960](assets/image-20230409221111960.png)

![image-20230409221128878](assets/image-20230409221128878.png)

刘东良为gitee的企业账号，osgisOne为我的Gitee的个人命名空间，所以出错！

![image-20230409221203640](assets/image-20230409221203640.png)

![image-20230409221221453](assets/image-20230409221221453.png)

![image-20230409221253617](assets/image-20230409221253617.png)

![image-20230409221350715](assets/image-20230409221350715.png)

![image-20230409221939154](assets/image-20230409221939154.png)

![image-20230409221956018](assets/image-20230409221956018.png)

#### SSH免密安全访问

![image-20230409223805631](assets/image-20230409223805631.png)

window 用户：dll,目录下.ssh
执行如下命令：

ssh-keygen -t rsa -C "602924803@qq.com"

![image-20230409224049545](assets/image-20230409224049545.png)

![image-20230409224117103](assets/image-20230409224117103.png)

#### ![image-20230409224141203](assets/image-20230409224141203.png)Git Bash操作

![image-20230409222650542](assets/image-20230409222650542.png)

![image-20230409224614623](assets/image-20230409224614623.png)

![image-20230409224946792](assets/image-20230409224946792.png)

![image-20230409225241730](assets/image-20230409225241730.png)

![image-20230409225211313](assets/image-20230409225211313.png)

假如没有Gitee多个账号，push不会失败，而是弹出输入账号、密码的对话框。pycharm通过插件可以保存凭据，对于不熟悉的人，会不知道如何操作。

Git bash也失败的原因，基本都是多个账号导致，这个可能window的凭据管理有关。

#### 我的仓库g0atm

参考我的仓库：https://gitee.com/chzuczldl/g0atm.git