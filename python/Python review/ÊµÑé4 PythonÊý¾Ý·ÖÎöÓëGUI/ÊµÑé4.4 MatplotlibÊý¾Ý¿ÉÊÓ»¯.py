#实验4.4 Matplotlib数据可视化

#（1）首先，在当前文件夹中生成WPF商店2018年营业额模拟数据文件data.csv
import csv,random,datetime
with open(r"data.csv","w+",newline='') as csvfile:#创建csv文件对象
    wr=csv.writer(csvfile,dialect="excel")#创建csv文件写入对象
    wr.writerow(["date","amount"])#写入标题：日期date、销量amount    
    startDate=datetime.date(2018,1,1)#初始日期2018-01-01    
    for i in range(365):#生成365个模拟数据，可以根据需要进行调整
        amount=int(random.random()*301+300)#生成一个销量模拟数据[300,600]，写入csv文件
        wr.writerow([startDate,amount])#写入数据
        startDate=startDate+datetime.timedelta(days=1)#下一天

#（2）然后，完成下面5项任务
import pandas as pd
import matplotlib.pyplot as plt

#1）使用pandas读取文件data.csv中的数据，创建DataFrame对象，并删除其中所有缺失值;
df=pd.read_csv("data.csv",encoding="cp936")#读取数据
df=df.dropna()#丢弃缺失值
#print(df);#print(df.describe())#describe()可进行缺失值分析与数据离散度分析

#2）按每天进行统计，使用matplotlib生成折线图，显示商店每天的销量情况，并把图形保存为本地文件day_amount_plot.png；
plt.figure(figsize=(12,6))#设置图片大小
plt.plot(df["date"],df["amount"],label="day->amount",color="red",linewidth=2)#作图(日期，销量)
plt.title("2018 Day Business Volume of Wpf Store")#设置图标题
plt.xlabel("day")#设置x轴名称
plt.ylabel("amount") #设置y轴名称
plt.xlim("2018-01-01","2018-12-31")#显示x轴范围
#plt.ylim(300,600)#显示y轴范围,默认从0开始
plt.legend()#刻印文字，生成图例,但不显示图片,可以替换label="Month->Amount"
plt.savefig("day_amount_plot.png")#注意顺序：先保存图，后显示
plt.show()#显示作图结果

#3）按月份进行统计，使用matplotlib生成柱状图，显示商店每月的销量情况，并把图形保存为本地文件second.png；
df1=df#初始化新df1
df1["month"]=df1["date"].map(lambda x: x[:x.rindex('-')])
df1=df1.groupby(by="month",as_index=False).sum()
#print(df1)#可查看df1的内容
plt.figure(figsize=(12,6))
plt.bar(df1["month"],df1["amount"],label="month->amount",color="blue")
plt.title("2018 Month Business Volume of Wpf Store")#设置图标题
plt.xlabel("month")#设置x轴名称
plt.ylabel("amount") #设置y轴名称
plt.xlim("2018-01","2018-12")#显示x轴范围
#plt.ylim(300,600)#显示y轴范围,默认从0开始
plt.legend()#刻印文字，生成图例,但不显示图片,可以替换label="Month->Amount"
plt.savefig("month_amount_bar.png")#注意顺序：先保存图，后显示
plt.show()#显示作图结果

#4）按月份进行统计，找出相邻两个月最大涨幅，并把涨幅最大的月份写入文件maxMonth.txt；
df2=df1.drop("month", axis=1).diff()
m=df2["amount"].nlargest(1).keys()[0]
with open("max_month.txt", 'w') as txtfile:
    txtfile.write(df1.loc[m,"month"])
txtfile.close()

#5）按季度进行统计，使用matplotlib生成饼状图，显示商店4个季度的销量分布情况，并把图形保存为本地文件third.jpg。
season1= df1[:3]['amount'].sum()    #第1季度（01-03月）数据统计
season2 = df1[3:6]['amount'].sum()  #第2季度（04-06月）数据统计
season3= df1[6:9]['amount'].sum()   #第3季度（07-09月）数据统计
season4= df1[9:12]['amount'].sum()  #第4季度（10-12月）数据统计
plt.figure(figsize=(12,6))
plt.pie([season1, season2, season3, season4],labels=["season1", "season2", "season3", "season4"])
plt.title("2018 Season Business Volume of Wpf Store")#设置图标题
plt.savefig('season_amount_pie.png')
plt.show()

csvfile.close()#关闭文件

