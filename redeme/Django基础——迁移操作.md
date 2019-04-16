### django的学习

#### 1.注册项目

**在settings.py里面**

INSTALLED_APPS里面添加

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


**注意**
```
后台管理语言设置：
1.8之前：
# LANGUAGE_CODE = 'en-us'
1.8之后
LANGUAGE_CODE = 'zh-hans'
```

![ ](https://upload-images.jianshu.io/upload_images/14371339-7824cd81fde1f4fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)