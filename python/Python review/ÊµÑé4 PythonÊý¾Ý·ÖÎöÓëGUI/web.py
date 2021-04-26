#实验5.4 Flask Web综合应用编程
'''
Web系统架构一般组成：
(1) 门户信息展示：index.html、show_test1.html、show_test2.html、show_test3.html等
(2) 前端用户平台：user_login.html、user_platform.html等
(3) 后台管理平台：admin_login.html、admin_platform.html等
(4) 其他信息提示：info.html、404.html等
'''
from flask import Flask,request,url_for,render_template,flash,abort

app=Flask(__name__)
app.secret_key="123" #任意密码，配合flash()一起关联使用

###########################################################################################################
#(1) 门户信息展示
@app.route('/') #一级路由
def index():
    title1="index"
    header1="Welcome to index page"
    content1="This is the index page!"
    content2=["hello python","hello wpf","hello kalof"]
    #渲染呈现门户信息主页index.html
    return render_template('/template/index.html',title=title1, header=header1, content=content1, contents=content2)

@app.route('/test1') #正向路由1
def test1():
    title1="show"
    header1="Welcome to show_test1 page"
    content1="This is the test1 page!"
    #渲染呈现模板生成网页show.html，模板显示信息子页show_test1.html
    return render_template('show_test1.html',title=title1, header=header1, content=content1)

@app.route('/test2') #正向路由2
def test2():
    title1="show"
    header1="Welcome to show_test2 page"
    content1="This is the test2 page!"
    #渲染呈现模板生成网页show.html，模板显示信息子页show_test2.html
    return render_template('show_test2.html',title=title1, header=header1, content=content1)

@app.route('/test3') #正向路由1
def test3():
    title1="show"
    header1="Welcome to show_test3 page"
    content1="This is the test3 page!"
    #渲染呈现模板生成网页show.html，模板显示信息子页show_test3.html
    return render_template('show_test3.html',title=title1, header=header1, content=content1)

###########################################################################################################
#前端用户平台
@app.route('/user_login') #二级路由
def user_login():
    #return "<a href='http://www.hzau.edu.cn'>hzau</a>"  #测试保留    
    title1="user_login"
    header1="Welcome to user_login page"
    content1="Hello wpf, this is the user login page!"
    #渲染呈现用户登录主页user_login.html
    return render_template('user_login.html',title=title1, header=header1, content=content1)

@app.route('/user_platform') 
def user_platform():    
    title1="user_platform"
    header1="Welcome to user_platform page"
    content1="Hello wpf, this is the user platform page!"
    #渲染呈现用户平台主页user_platform.html
    return render_template('user_platform.html',title=title1, header=header1, content=content1)

@app.route('/user/<uid>', methods=['GET','POST']) #路由传参方法一  例如：'users/123'
def user_id(uid):
    title1="query_user"
    header1="Welcome to query_user page"
    content1="Hello wpf, this is the query user page!"
    content2="query user:"+ uid
    #渲染呈现参数传递子页query_user.html
    return render_template('query_user.html',title=title1, header=header1, content1=content1, content2=content2)

@app.route('/query_user', methods=['GET','POST']) #路由传参方法二 例如：'query_users?uid=123'
def query_user_uid():
    try:
        uid=request.args.get("uid")
        uname=request.args.get("uname")
        if int(uid): #判断必须是整数
            title1="query_user"
            header1="Welcome to query_user page"
            content1="Hello wpf, this is the query user page!"
            if uname:
                content2="query user: id="+ uid + ", " +"name=" + uname
            else:
                content2="query user: id="+ uid
            #渲染呈现参数传递子页query_user.html
            return render_template('query_user.html',title=title1, header=header1, content1=content1, content2=content2)
        else:
            abort(500)  #否则提交500错误中止码
    except:
        abort(500)  #否则提交500错误中止码

@app.route('/query_url') #反向路由
def query_url():
    #查找到对应url地址        
    title1="query_url"
    header1="Welcome to query_url page"
    content1="Hello wpf, this is the query url page!"
    content2="query url:"+ url_for('user_login')
    #渲染呈现反向路由子页query_url.html
    return render_template('query_url.html',title=title1, header=header1, content1=content1, content2=content2)

###########################################################################################################
#后台管理平台
@app.route('/admin_login', methods=['GET','POST']) #二级路由
def admin_login():
    #return "<a href='http://www.hzau.edu.cn'>hzau</a>"  #测试保留    
    title1="admin_login"
    header1="Welcome to admin_login page"
    content1="Hello wpf, this is the admim login page!"
    #渲染呈现管理登录主页admin_login.html
    return render_template('admin_login.html',title=title1, header=header1, content=content1)

@app.route('/admin_platform') 
def admin_platform():    
    title1="admin_platform"
    header1="Welcome to admin_platform page"
    content1="Hello wpf, this is the admin platform page!"
    #渲染呈现管理平台主页admin_platform.html
    return render_template('admin_platform.html',title=title1, header=header1, content=content1)

###########################################################################################################
#其他信息提示
@app.route('/info')
def info():
    title1="info"
    header1="Welcome to info page"
    flash("Hello python3 and wpf!") #代替content, 需要关联app.secret_key="123"配合使用
    #渲染呈现其他信息子页info.html
    return render_template('info.html',title=title1, header=header1)

@app.errorhandler(404) #错误句柄,提示404错误信息
def not_found1(e):
    title1="error:404"
    header1="Welcome to error:404 page"
    content1="This page went to Mars!"
    #渲染呈现错误信息子页404.html
    return render_template('404.html',title=title1, header=header1, content=content1)

@app.errorhandler(500) #错误句柄,提示500错误信息
def not_found2(e):
    title1="error:500"
    header1="Welcome to error:500 page"
    content1="This page has been aborted!"
    #渲染呈现错误信息子页500.html
    return render_template('500.html',title=title1, header=header1, content=content1)
    
###########################################################################################################
#主程序入口
if __name__=="__main__":
    app.run(host="127.0.0.1",port=8081)