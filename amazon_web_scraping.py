from bs4 import BeautifulSoup
import requests
import datetime
import time

import smtplib 
# USED FOR SENDING MAILS BUT HERE WE HAVE NOT USED IT...


url = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

hdrs={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page=requests.get(url,headers=hdrs)

soup1=BeautifulSoup(page.content,'html.parser')
soup2=BeautifulSoup(soup1.prettify(),'html.parser')
print('-----------------------------------------------------')
title=soup2.find(id='productTitle').get_text()
title2=soup2.find(id='bylineInfo').get_text()
print(title)
print(title2)
print('-----------------------------------------------------')
# making data more cleaner by removing extra spaces
title=title.strip()
title2=title2.strip()
print(title)
print(title2)
print('-----------------------------------------------------')

# fetching present date from datetime module
today=datetime.date.today()
print(today)
print('-----------------------------------------------------')

# now importing csv to write imported data into csv files
import csv

header=['Title1','Title2','Date']
data=[title,title2,today]
with open('Amazon_Web_Scraper_Dataset.csv','w',newline='',encoding='UTF8') as f:
    wrtr = csv.writer(f)
    wrtr.writerow(header)
    wrtr.writerow(data)


# for checking data that is stored in csv we can import pandas
import pandas as pd

pd.set_option('display.max.columns',10)
df=pd.read_csv(r'D:\BVP SSB\Data Analysis\Python\Amazon_Web_Scraper_Dataset.csv')
print(df)
print('-----------------------------------------------------')
