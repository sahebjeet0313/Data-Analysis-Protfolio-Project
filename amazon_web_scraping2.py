from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def get_title(soup):
    try:
        title=soup.find_all('span', id="productTitle" )
        title_data=[tt.text.strip() for tt in title]
        # print(title_data)
    except AttributeError:
        title_data=''
    return title_data
    # print('-------------------------------')

def get_price(soup):
    try:
        price = soup.find_all('span',class_="a-offscreen")[0]
        price_data=[tt.text for tt in price]
        # print(price_data)
    except AttributeError:
        price_data=''
    return price_data
    # print('-------------------------------')

def get_ratings(soup):
    try:
        ratings= soup.find_all('span', class_="a-icon-alt")[0]
        ratings_data=[tt.text.strip() for tt in ratings]
        # print(ratings_data)
    except AttributeError:
        ratings_data=''
    return ratings_data
    # print('-------------------------------')

if __name__=='__main__':
    url ='https://www.amazon.in/s?k=boat+smart+watch&sprefix=boat+sma%2Caps%2C210&ref=nb_sb_ss_ts-doa-p_1_8'
    hdrs=({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
    page=requests.get(url,headers=hdrs)
    soup=BeautifulSoup(page.text,'html.parser')
    # print(soup)
    link = soup.find_all('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    # print(link[0].get('href'))
    links_list=[]
    
    for i in link:
        links_list.append(i.get('href'))
    
    d={'title':[],'price':[],'ratings':[]}
    
    for i in links_list:
        # print('-------------------------------')
        # print(new_webpage)
        # print('-------------------------------')
        new_page=requests.get('https://www.amazon.in' + i,headers=hdrs)
        new_soup=BeautifulSoup(new_page.text,'html.parser')
        # print(new_soup)
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['ratings'].append(get_ratings(new_soup))

    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data_ssb.csv", header=True, index=False)
    print(amazon_df)
