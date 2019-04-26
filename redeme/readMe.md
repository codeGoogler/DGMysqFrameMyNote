### django的学习

#### 1.注册项目  

**在settings.py里面**

INSTALLED_APPS

#### 2、生成迁移

python manage.py makemigrations

#### 4、执行迁移

python manage.py migrate

#### 5、测试数据库操作

python manage.py shell

* 1、引入模块
* 2. 要注意的是：咋数据库model中添加方法，不需要重新迁移


### django的管理

* 创建一个用户管理员

python manage.py createsuperuser ,按照提示输入用户名，密码，邮箱

* 启动服务器，通过 '127.0.0.1:8000/admin',输入创建的的用户名，密码完成登录’

* 进入管路站点，默认可以对groups.users进行 管理



# 解绑一个学习地址
https://code.ziqiangxuetang.com/django/django-views-urls.html




到这里我们差不多就知道了，python manage.py makemigrations这个命令是记录我们对models.py的所有改动，并且将这个改动迁移到migrations这个文件下生成一个文件例如：0001文件，如果你接下来还要进行改动的话可能生成就是另外一个文件不一定都是0001文件，但是这个命令并没有作用到数据库，这个刚刚我们在上面的操作过程之后已经看到了，而当我们执行python manage.py migrate 命令时  这条命令的主要作用就是把这些改动作用到数据库也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，或者增加字段属性

另外一个需要注意的是这两个命令默认情况下是作用于全局，也就是对所有最新更改的models或者migrations下面的迁移文件进行对应的操作，如果要想仅仅对部分app进行作用的话  则执行如下命令：

* python manage.py makemigrations appname,

* python manage.py migrate appname,

如果要想精确到某一个迁移文件则可以使用：

python manage.py migrate appname 文件名
--------------------- 
作者：leeyongbard 
来源：CSDN 
原文：https://blog.csdn.net/hpu_yly_bj/article/details/78928089 
版权声明：本文为博主原创文章，转载请附上博文链接！