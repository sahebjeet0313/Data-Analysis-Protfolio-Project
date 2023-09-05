from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)

soup=BeautifulSoup(page.text,'html.parser')
# print(soup.find_all('table',class_='wikitable sortable'))
table=soup.find_all("table")[1]

world_title=table.find_all("th")

world_table_title=[title.text.strip() for title in world_title]

# print(world_table_title)

df = pd.DataFrame(columns=world_table_title)

column_data= table.find_all('tr')

for i in column_data[1:]:
    row_data=i.find_all('td')
    world_table_data=[data.text.strip() for data in row_data]
    # print(world_table_data)
    
    length = len(df)
    df.loc[length]=world_table_data

print(df)
    

df.to_csv(r'D:\BVP SSB\Data Analysis\Python\Files\Files For Output\World_Data.csv')
