import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random   #定义随机生成颜色函数
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color ="#"+''.join([random.choice(colorArr) for i in range(6)])
    return color

xlsx_file='零新增天数.xlsx'

df = pd.read_excel(xlsx_file, usecols=[0,1])
df = df.sort_values(by='天数',ascending=False)
num=df.shape[0]



plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

r = np.array([df.loc[i][1] for i in range(num)])
theta = np.arange(0,2*np.pi ,2*np.pi/num )
colors = np.array([randomcolor() for i in range(num)])

plt.figure(figsize=(30,10),dpi=80)
plt.axes(projection='polar')
for n in range(num):
 n=plt.bar(theta[n]+np.pi/2,r[n],width=2*np.pi/num, color=colors[n], alpha=1)
plt.legend(loc='upper right') 
plt.legend(labels=np.array([df.loc[i][0] for i in range(num)]), loc='center right')
plt.title('零新增天数玫瑰图', pad=15)

plt.show()

    

    
                  
                    