import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random   #定义随机生成颜色函数
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color ="#"+''.join([random.choice(colorArr) for i in range(6)])
    return color
def ave_month(list_mon):
    all=0
    for i in list_mon:
        all+=i
    ave=all/len(list_mon)
    return int(ave)

xlsx_file='广州历史天气.xlsx'
high=[]
low=[]
df = pd.read_excel(xlsx_file, usecols=[2,3,4])
for i in range(df.shape[0]):
 df['标题1'][i]=df['标题1'][i][0:10]
 df['字段'][i]= df['字段'][i][0:-1]
 df['字段1'][i] = df['字段1'][i][0:-1]
df['标题1'] = pd.to_datetime(df['标题1'])
df = df.sort_values(by='标题1',ascending=True)
df.to_excel('weather.xlsx',sheet_name = "天气",index = False,na_rep = 0,inf_rep = 0)
for index in range(0,df.shape[0]-31,30):
    list_mon=[]
    for i in range(index,index+30):
        list_mon.append(int(df['字段'][i]))
    
    high.append(ave_month(list_mon=list_mon))

for index in range(0,df.shape[0]-31,30):
    list_mon=[]
    for i in range(index,index+30):
        list_mon.append(int(df['字段1'][i]))
    
    low.append(ave_month(list_mon=list_mon))

x_1 = np.array(high)
x_2=np.array(low)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.title("广州月平均气温变化图")
plt.xlabel('时间/月')
plt.ylabel("气温/°C")

p1=plt.plot(x_1,'r')
p2=plt.plot(x_2,'b')

plt.grid()

plt.show()
