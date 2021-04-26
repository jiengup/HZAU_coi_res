#实验4.5 成绩统计-简单GUI编程
from tkinter import *
from tkinter import messagebox
class ScoreCalculate:
    def __init__(self):
        win = Tk()
        win.geometry("280x220")
        win.title("学生成绩统计")
        
        lblCpp=Label(win, text="C/C++程序设计")#创建Label标签
        lblCpp.grid(row=0, column=0, padx=5, pady=5, sticky="e")#使用grid进行布局
        self.vCpp=IntVar();
        self.vCpp.set(90) #使用self，并设置初值
        entCpp=Entry(win, width=15, textvariable=self.vCpp)#创建Entry对象
        entCpp.grid(row=0, column=1, padx=5, pady=5, sticky="w")#使用grid进行布局

        lblPython=Label(win,text="Python程序设计")
        lblPython.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.vPython=IntVar();
        self.vPython.set(96)
        entPython=Entry(win, width=15, textvariable=self.vPython)
        entPython.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        lblJava=Label(win, text="Java程序设计")
        lblJava.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.vJava=IntVar();
        self.vJava.set(88)
        entJava=Entry(win, width=15, textvariable=self.vJava)
        entJava.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        lblIoT=Label(win, text="物联网工程")
        lblIoT.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.vIoT=IntVar();
        self.vIoT.set(98)
        entIoT=Entry(win, width=15, textvariable=self.vIoT)
        entIoT.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        btnCalculate=Button(win, text="计算平均成绩", command=self.Calculate)
        btnCalculate.grid(row=4, column=0, columnspan=2, pady=5)
        
        lblAvg= Label(win, text="平均成绩:")
        lblAvg.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.vAvg=DoubleVar()#有精度
        entAvg=Entry(win, width=15, state="readonly",textvariable=self.vAvg)#显示数据 
        entAvg.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        win.mainloop()

    def Calculate(self):
        try:
            xCpp=float(self.vCpp.get())#获取C++成绩
            xPython=float(self.vPython.get())#获取Python成绩            
            xJava=float(self.vJava.get())#获取Java成绩
            xIoT=float(self.vIoT.get())#获取IoT成绩
            xAvg=(xCpp + xPython + xJava + xIoT)/4           
            self.vAvg.set(round(xAvg, 1))#保留1位小数并输出            
        except:
            messagebox.showerror(title="提示", message="输入错误，请重新输入")
            
ScoreCalculate()




