#实验5.4 综合Web编程-Flask框架
#Flask是轻量级非全栈Non-Full Stack Web开发框架
#程序代码在flask_web目录中
'''
flask_web目录说明
(1) flask_web目录：用户自己创建根目录，
    其中包含自创建flask_web.py文件和自创建templates子目录
(2) flask_web.py文件:文件名创建时可修改，一般web框架由4部分组成：
    门户信息展示、前端用户平台、后台管理平台、其他信息提示
    
(2) templates目录：是flask_web子目录,且必须是该目录名，存放所有*.html网页
    门户信息展示包含网页文件有5个等：
    index.html:门户信息主页
    show.html :模板生成子页
    show_test1.html:信息显示子页
    show_test2.html:信息显示子页
    show_test3.html:信息显示子页    

    前端用户平台包含网页文件有4个等：
    user_login.html:用户登录主页
    user_platform.html:用户平台主页    
    query_user.html:参数传递子页
    query_url.html :反向路由子页    

    后台管理平台包含网页文件有2个等：
    admin_login.html:管理登录主页
    admin_platform.html:管理平台主页

    其他信息提示包含网页文件有3个等：
    info.html:其他信息子页
    404.html :错误信息子页
    500.html :错误信息子页
'''
"""
执行flask_web.py，启动Web服务并开启程序路由功能。
在浏览器可直接输入：http://127.0.0.1:8081/启动运行，浏览效果正常即可。
"""

