#实验4.3 Pandas数据分析

#（1）创建3个一级索引的Series数据结构
from pandas import Series #从pandas库中引用Series
print("创建3个一级索引的Series数据结构：",end='\n')
obj_list=[98,88,78,68]
obj_tuple=("C++程序设计","Python程序设计","Java程序设计","物联网工程")
obj_dict={"201801":["张珊",18,"女","计算机1801"],
          "201802":["李斯",19,"男","计算机1802"],
          "201803":["王武",18,"男","计算机1803"],
          "201804":["赵柳",19,"女","计算机1804"]}
series_list=Series(obj_list,index=["No1","No2","No3","No4"])
series_tuple=Series(obj_tuple,index=["cId0001","cId0002","cId0003","cId0004"])
series_dict=Series(obj_dict)
print("(1)通过列表创建第一个Series数据结构：");print(series_list)
print("(2)通过元组创建第二个Series数据结构：");print(series_tuple)
print("(3)通过字典创建第三个Series数据结构：");print(series_dict)

print("----------------------------------------")
#（2）创建2个二级索引(行索引和列索引)的DataFrame数据结构
from pandas import DataFrame #从pandas库中引用DataFrame
print("创建2个二级索引的DataFrame数据结构：",end='\n')
obj1={"学号":["201801","201802","201803","201804","201801"],
     "姓名":["张珊","李斯","王武","赵柳","周琪"],
     "年龄":[18,19,19,18,18],
     "性别":["女","男","男","女","女"],
     "班级":["计算机1801","计算机1802","计算机1803","计算机1804","计算机1801"]
     }
dataframe_obj1=DataFrame(obj1)
print("(1)通过字典创建第一个DataFrame数据结构（学生信息）：")
print(dataframe_obj1)

series_list1=Series(["2001020","张珊",38,"女","副教授"],index=["工号","姓名","年龄","性别","职称"])
series_list2=Series(["2001021","李斯",39,"男","副教授"],index=["工号","姓名","年龄","性别","职称"])
series_list3=Series(["2001023","王武",39,"男","副教授"],index=["工号","姓名","年龄","性别","职称"])
series_list4=Series(["2001024","赵柳",38,"女","副教授"],index=["工号","姓名","年龄","性别","职称"])
series_list5=Series(["2001025","周琪",38,"女","副教授"],index=["工号","姓名","年龄","性别","职称"])
dataframe_obj2=DataFrame([series_list1,series_list2,series_list3,series_list4,series_list5])
print("(2)通过Series创建第二个DataFrame数据结构（教师信息）：")
print(dataframe_obj2)
