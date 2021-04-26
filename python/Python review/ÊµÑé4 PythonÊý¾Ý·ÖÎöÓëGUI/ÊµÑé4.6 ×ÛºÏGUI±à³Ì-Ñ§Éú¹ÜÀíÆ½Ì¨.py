#实验4.6 综合GUI编程-学生管理平台

import tkinter as Tk
from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os

################################################################################
import tkinter as Tk
class sLogin:
    """登录界面"""
    #----------------------------------------------------------------------
    def __init__(self, login):#构造初始
        """登录界面初始"""
        self.frmLogin=login
        self.frmLogin.geometry("320x200+380+200")
        self.frmLogin.title("用户登录")
        self.frame=Tk.Frame(self.frmLogin) #windows开发：frame, web开发：(page)
        self.gridFrame()
       
    #----------------------------------------------------------------------
    def gridFrame(self):#界面布局
        """登录界面布局"""
        self.uid=StringVar(); self.uid.set("wpf")
        self.upwd=StringVar(); self.upwd.set("123")
        
        Label(self.frame).grid(row=0)#让界面先空一行
        Label(self.frame, text="学生管理平台", fg="blue", font=("黑体",20,"bold")).grid(row=1, columnspan=2)
        Label(self.frame, text="用户名", width=5).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        Entry(self.frame, textvariable=self.uid).grid(row=2, column=1, pady=10, sticky='w')
        Label(self.frame, text="密   码",width=5).grid(row=3, column=0, padx=10, pady=5,  sticky='e')        
        Entry(self.frame, textvariable=self.upwd, show='*').grid(row=3, column=1, pady=5, sticky='w')
        Button(self.frame,text="登录", width=13,
               command=self.onLogin).grid(row=4, column=0, pady=10, sticky='w')
        Button(self.frame,text="退出", width=13,
               command=self.onExit).grid(row=4, column=1, pady=5, sticky='e' )        
        self.frame.pack()
        
    #----------------------------------------------------------------------
    def onLogin(self):
        """登录进入"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        cmd=self.conn.cursor()
        sql="select uid, upwd from user where uid='%s'" % self.uid.get()
        cmd.execute(sql)  #执行数据库
        ds=cmd.fetchall() #接收全部信息
        if len(ds)==0:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("登录失败", "账户不存在")
        else:
            xuid, xupwd = ds[0]
            if xuid==self.uid.get() and xupwd==self.upwd.get():
                self.hide() #隐藏窗体
                root=Tk.Tk() #主窗体，作为一级窗体比较合适
                sMain(root)
                root.mainloop()                
            else:
                messagebox.showwarning("登录失败", "密码错误")
        self.conn.close() #关闭数据库

    #----------------------------------------------------------------------
    def hide(self):
        """隐藏窗体"""
        self.frame.destroy()
        self.frmLogin.withdraw()
    
    #----------------------------------------------------------------------            
    def onExit(self): 
        """退出登录"""        
        os._exit(0)#退出系统    

################################################################################
import tkinter as Tk
class sMain(object):
    """主控界面"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        self.root=parent
        self.root.geometry("1220x600+20+10")
        self.root.title("学生管理平台v1.0")
        self.frame=Tk.Frame(self.root)        
        self.menuFrame()

    #----------------------------------------------------------------------
    def menuFrame(self):
        """设计菜单"""
        self.main=Tk.Menu(self.root)#创建主菜单
        #self.subMenu1=Menu(self.main)   #创建下拉子菜单1：学生管理
        #self.subMenu2=Menu(self.main)   #创建下拉子菜单2：课程管理
        self.subMenu3=Menu(self.main)    #创建下拉子菜单3：成绩管理        
        self.subMenu3.add_command(label="录入成绩")
        self.subMenu3.add_command(label="查询成绩")
        self.subMenu3.add_command(label="统计成绩", command=self.onCalScore)
        self.main.add_cascade(label="学生管理", command=self.onOpenStudent)
        self.main.add_cascade(label="课程管理")
        self.main.add_cascade(label="成绩管理", menu=self.subMenu3)
        self.main.add_cascade(label="退出系统", command=self.onExit)
        self.root["menu"]=self.main #显示菜单
        self.frame.pack()
        
    #----------------------------------------------------------------------   
    def onOpenStudent(self):
        """打开子窗体"""
        sub=Tk.Toplevel()#弹出顶级窗体，作为二级子窗体比较合适
        #sub=Tk.Tk()     #主窗口，一般作为一级窗口
        sManage(sub)
    
    #----------------------------------------------------------------------   
    def onCalScore(self):
        """统计成绩"""
        pass

    #----------------------------------------------------------------------  
    def onExit(self):
        """退出系统"""
        os._exit(0)#退出系统

################################################################################
import tkinter as Tk
class sManage():
    """学生管理"""
    #----------------------------------------------------------------------
    def __init__(self, child):
        """学生界面初始"""
        self.frmStudent=child
        self.frmStudent.geometry("600x400+40+70")
        self.frmStudent.title("学生管理")
        self.frame=Tk.Frame(self.frmStudent)        
        self.gridFrame()
        
    #----------------------------------------------------------------------
    def gridFrame(self):
        """学生界面布局"""
        self.sid=StringVar(); self.sid.set('')
        self.sname=StringVar(); self.sname.set('')
        self.ssex=StringVar(); self.ssex.set('')
        self.sage=StringVar(); self.sage.set('')# 编程心得：年龄类型也做成字符串
        self.sclass=StringVar(); self.sclass.set('')

        #必须使用grid布局网格，配合使用place精确定位
        Label(self.frame).grid(row=0)#界面空一行
        Label(self.frame, text="学生管理平台", fg="blue",
              font=("黑体",20,"bold")).grid(row=1, columnspan=4)#使用grid布局
        Label(self.frame, text="学  号", fg="red").grid(row=2, column=0, pady=5, sticky='w')
        Entry(self.frame, textvariable=self.sid).place(x=48, y=63) #使用place定位       
        Label(self.frame, text="姓  名").grid(row=3, column=0, pady=5, sticky='w')        
        Entry(self.frame, textvariable=self.sname).place(x=48, y=96)#使用place定位 
        Label(self.frame, text="性  别").place(x=231, y=96) #使用place定位        
        Entry(self.frame, textvariable=self.ssex).place(x=281, y=96)#使用place定位
        Label(self.frame, text="年  龄").grid(row=4, column=0, pady=5, sticky='w')        
        Entry(self.frame, textvariable=self.sage).place(x=48, y=129)#使用place定位 
        Label(self.frame, text="班  级").place(x=231, y=129) #使用place定位        
        Entry(self.frame, textvariable=self.sclass).place(x=281, y=129)#使用place定位
        Button(self.frame,text="录入", width=10, command=self.onInsert).place(x=0, y=165)#使用place定位
        Button(self.frame,text="删除", width=10, command=self.onDelete).place(x=85, y=165)
        Button(self.frame,text="修改", width=10, command=self.onUpdate).place(x=170, y=165)
        Button(self.frame,text="查询", width=10, command=self.onSelect).place(x=255, y=165)
        Button(self.frame,text="查看", width=10, command=self.onLook).place(x=340, y=165)
        Button(self.frame,text="关闭", width=10, command=self.onHide).place(x=425, y=165)
        self.vShow=StringVar();
        self.vShow.set('')
        #Text(self.frame,textvariable=self.v,width=60,height=23).grid(row=5,columnspan=4,pady=50,sticky='e')
        Listbox(self.frame, listvariable=self.vShow,
                width=72, height=9).grid(row=5, columnspan=4, pady=50, sticky='e')#height:是行数        
        self.frame.pack()

    #----------------------------------------------------------------------
    def onInsert(self):
        """录入学生"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        self.cmd=self.conn.cursor()
        
        #检查记录是否存在，不存在才能录入新学生记录
        sql="select sid, sname, ssex, sage, sclass from student where sid='%s'"%self.sid.get()
        self.cmd.execute(sql)  #执行数据库
        ds=self.cmd.fetchall() #接收全部信息
        if len(ds)==1:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("录入失败","学生" + self.sid.get() + "存在，不允许重复录入...")
        else:
            sql="insert into student(sid,sname,ssex,sage,sclass) values('%s','%s','%s','%s','%s')" \
                 %(self.sid.get(),self.sname.get(),self.ssex.get(),self.sage.get(),self.sclass.get())
            self.cmd.execute(sql)            
            self.conn.commit()#提交数据
            messagebox.showinfo("录入成功","录入学生" + self.sid.get() + "成功...")
        self.cmd.close()
        self.conn.close() #关闭数据库
        
    #----------------------------------------------------------------------
    def onDelete(self):
        """删除学生"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        self.cmd=self.conn.cursor()
        
        #检查记录是否存在，存在才能删除学生记录
        sql="select sid, sname, ssex, sage, sclass from student where sid='%s'"%self.sid.get()
        self.cmd.execute(sql)  #执行数据库
        ds=self.cmd.fetchall() #接收全部信息
        if len(ds)==0:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("删除失败","学生" + self.sid.get() + "不存在，删除失败...")
        else:
            sql="delete from student where sid='%s'"%self.sid.get()
            self.cmd.execute(sql)            
            self.conn.commit()#提交数据
            messagebox.showinfo("删除成功","删除学生" + self.sid.get() + "成功...")
        self.cmd.close()
        self.conn.close() #关闭数据库

    #----------------------------------------------------------------------
    def onUpdate(self):
        """修改学生"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        self.cmd=self.conn.cursor()
        
        #检查记录是否存在，存在才能修改学生记录
        sql="select sid, sname, ssex, sage, sclass from student where sid='%s'"%self.sid.get()
        self.cmd.execute(sql)  #执行数据库
        ds=self.cmd.fetchall() #接收全部信息
        if len(ds)==0:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("修改失败","学生" + self.sid.get() + "不存在，修改失败...")
        else:
            sql="update student set sname='%s', ssex='%s', sage='%s', sclass='%s' where sid='%s'" \
            %(self.sname.get(),self.ssex.get(),self.sage.get(),self.sclass.get(),self.sid.get())
            self.cmd.execute(sql)            
            self.conn.commit()#提交数据
            messagebox.showinfo("修改成功","修改学生" + self.sid.get() + "成功...")
        self.cmd.close()
        self.conn.close() #关闭数据库

    #----------------------------------------------------------------------
    def onSelect(self):
        """查询学生"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        self.cmd=self.conn.cursor()
        sql="select sid, sname, ssex, sage, sclass from student where sid='%s'"%self.sid.get()
        self.cmd.execute(sql)  #执行数据库
        ds=self.cmd.fetchall() #接收全部信息
        if len(ds)==0:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("查询失败","查询学生" + self.sid.get() + "不存在...")
        else:
            xsid, xsname, xssex, xsage, xsclass = ds[0]
            self.sid.set(xsid)
            self.sname.set(xsname)
            self.ssex.set(xssex)
            self.sage.set(xsage)
            self.sclass.set(xsclass)
            strResult=xsid+','+xsname+','+xssex+','+xsage+','+xsclass #注意：不用空格，而用逗号分隔
            self.vShow.set(strResult) #列表框中以空格分割元素进入列表中        
        self.cmd.close()
        self.conn.close() #关闭数据库

    def onLook(self):
        """查看学生"""
        self.conn=sqlite3.connect("test.db")#连接数据库        
        self.cmd=self.conn.cursor()
        sql="select sid, sname, ssex, sage, sclass from student"
        self.cmd.execute(sql)  #执行数据库
        ds=self.cmd.fetchall() #接收全部信息
        if len(ds)==0:  #值为0，表示没有找到记录, 值为1，表示有一条记录
            messagebox.showerror("查看失败","查询学生" + self.sid.get() + "不存在...")
        else:
            strResult=''
            for i in range(len(ds)):
                xsid, xsname, xssex, xsage, xsclass = ds[i]
                strResult+=xsid+','+xsname+','+xssex+','+xsage+','+xsclass+' ' #注意：不用空格，而用逗号分隔
            self.vShow.set(strResult) #列表框中以空格分割元素进入列表中        
        self.cmd.close()
        self.conn.close() #关闭数据库

    #----------------------------------------------------------------------
    def onHide(self):
        """隐藏窗体"""
        self.frame.destroy()
        self.frmStudent.withdraw()

################################################################################
import tkinter as Tk
if __name__=="__main__":
    """主程序启动入口"""
    login=Tk.Tk()
    sLogin(login)#登录窗体为第一启动对象       
    login.mainloop()



