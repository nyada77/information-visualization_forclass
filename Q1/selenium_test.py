from lxml import etree
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

list_all=[]#二维列表表示数据全集
list_href=[]
broswer= webdriver.Chrome()

 
def click():
 next_ = broswer.find_element(By.CLASS_NAME,'lishidesc2')
 next_.click()
 
def data_get(source):
 
 html=etree.HTML(source)
 li_list=html.xpath('/html/body//ul[@class="thrui"]//li')
 for li in li_list: 
    list_all.append(li.xpath('.//div/text()'))
   
def main(city):      
 for year in range(2022,2010,-1):
   for month in range(1,13):
      if month<10:
       list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+'0'+str(month)+'.html')
      else:
         list_href.append('https://lishi.tianqi.com/'+city+'/'+str(year)+str(month)+'.html')  
 for href in list_href:
  try:
   broswer.get(href) 
  except:
    continue
  click()
  source=broswer.page_source
  data_get(source)
  time.sleep(5)
  print(list_all)
  
 to_csv(list_all)
 return 0


def to_csv(list_all):
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
 df.to_csv('./yangjiang_wea.csv')
  
main('yangjiang')


