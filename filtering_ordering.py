import pandas as pd

df=pd.read_csv(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output\world_population.csv")

pd.set_option("display.max.rows",500)
pd.set_option("display.max.columns",20)

# print(df)
print('--------------------------------------------------------------------------------------------------------------------------------')
# filltering csv files 
rank_less_than_10= df[df['Rank'] <10]
print(rank_less_than_10)
print('--------------------------------------------------------------------------------------------------------------------------------')
# searching by using isin function
specific_countries = ['Bangladesh','Brazil','India']
specific_country_data = df[df['Country'].isin(specific_countries)]
print(specific_country_data)
print('--------------------------------------------------------------------------------------------------------------------------------')
# searching substring by using str.contains
print(df[df['Country'].str.contains('United')])
print('--------------------------------------------------------------------------------------------------------------------------------')

# setting index to country
df2=df.set_index("Country")
# applying filters
df3=df2.filter(items=['Continent','CCA3','2020 Population'])
print(df3)
print('--------------------------------------------------------------------------------------------------------------------------------')
# searching any particular string without knowing its heading or title
df4=df2.filter(items=['India'],axis=0)
print(df4)
print('--------------------------------------------------------------------------------------------------------------------------------')
# or alternative way is by using like
df5=df2.filter(like='United',axis=0)
print(df5)
print('--------------------------------------------------------------------------------------------------------------------------------')
# we can also search by using loc function 
# loc searches directly string values provided 
# iloc only searches for inteeger values
print(df2.loc[['India']])
print('--------------------------------------------------------------------------------------------------------------------------------')

# using order by function

print(df2[df2["Rank"]<10].sort_values(by='Rank',ascending=False))
print('--------------------------------------------------------------------------------------------------------------------------------')
