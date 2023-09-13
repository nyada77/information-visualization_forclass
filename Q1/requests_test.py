#代码食用方法：在最后面的main（）里面加入你想要爬取的城市参数
import requests
from lxml import etree
import time
import pandas as pd
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 发送请求
def main(city):
 list_href=[]
 list_all=[] 
 for year in range(2011,2023):
   for month in range(1,13):
      if month<10:
       list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+'0'+str(month)+'.html')
      else:
         list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+str(month)+'.html')  
 for href in list_href:
  try:
   response=requests.get(href,headers=headers)
   print(response.status_code,end=' ')
   source=response.text
   data_get(source,list_all)
   time.sleep(3)
  except:
     to_csv(list_all,city)
     return 0
  to_csv(list_all,city)
  
def data_get(source,list_all):
 html=etree.HTML(source)
 li_list=html.xpath('/html/body//ul[@class="thrui"]//li')
 for li in li_list: 
    list_all.append(li.xpath('.//div/text()'))
    

def to_csv(list_all,city='Unkown'):
 load='./'+city+'_wea.csv'
 dic_all={}
 value_date=[]
 value_highest=[]
 value_lowest=[]
 value_weather=[]
 value_wind=[]
 for day in list_all:
  value_date.append(day[0])
  value_highest.append(day[1])
  value_lowest.append(day[2])
  value_weather.append(day[3])
  value_wind.append(day[4])
 dic_all['date']=value_date
 dic_all['highest']=value_highest
 dic_all['lowest']=value_lowest
 dic_all['weather']=value_weather
 dic_all['wind']=value_wind
 df=pd.DataFrame(dic_all)#df方法传入字典时其value必须是可迭代序列（如列表）
 df.to_csv(load)
 
 
 
main('weihai')