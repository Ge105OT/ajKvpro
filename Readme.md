﻿# 需要的模块：pycrypto，pyqt4

# 功能：
&nbsp;&nbsp;    1、固定的数据库保存着用户名及其密码，密码经过MD5，登录通过MD5验证。<br>
&nbsp;&nbsp;    2、一个用户有多个表，其中创建时会创建一个base的表，保存基本的账号密码，<br>
&nbsp;&nbsp;      并创建一个tables表保存其他账号密码表的属性信息，为扩展使用。<br>
&nbsp;&nbsp;    3、用户密码的密码都使用aes加密，其密钥是登录用户密码+用户名的MD5，iv是登录用户名+数据库名的MD5再计算，<br>
&nbsp;&nbsp;      这样更能保证密码的安全。<br>
&nbsp;&nbsp;    4、注册的账号不能相同，可以注册多个账号，其密码要求8-16位字母数字(可加特殊字符)组合。<br>
&nbsp;&nbsp;    5、可以查询保存的账号及其密码，输出在log窗口<br>
&nbsp;&nbsp;    6、提供锁屏功能<br>
&nbsp;&nbsp;    7、提供额外工具：随机密码生成器<br>
&nbsp;&nbsp;    8、可修改界面上几个窗口大小<br>
&nbsp;&nbsp;    9、有快捷键、鼠标右键菜单、日志输出、状态栏显示<br>

# 为学习程序ui设计，学习pyqt，并能使用上程序，设计了密码管理器，保存管理个人账户密码。

# login
&nbsp;&nbsp;登陆界面，右下方新用户点击可以创建一个新的用户<br>
![login](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/log.png?raw=true)

# main
&nbsp;&nbsp;主界面，登陆初始状态下<br>
![main](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/main.png?raw=true)

# main1
&nbsp;&nbsp;主界面，登陆后点击其中某一个表下<br>
![main1](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/main1.png?raw=true)

# menu
&nbsp;&nbsp;其中在tablewidget下的右击菜单，另一个在treewidget的右击菜单则不贴图了<br>
![menu](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/menu.png?raw=true)

# newrecord
&nbsp;&nbsp;新增账号密码<br>
![newrecord](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/newrecord.png?raw=true)

# lock
&nbsp;&nbsp;锁屏界面<br>
![lock](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/lock.png?raw=true)

# random
&nbsp;&nbsp;主界面，登陆初始状态下<br>
![random](https://github.com/Ge105OT/ajKvpro/blob/master/exeimg/random.png?raw=true)
