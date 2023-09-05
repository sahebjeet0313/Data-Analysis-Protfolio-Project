import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output\world_population.csv")
pd.set_option('display.max.columns',20)
print('--------------------------------------------------------------')
print(df)
print('--------------------------------------------------------------')
print(df.info())
print('--------------------------------------------------------------')
print(df.describe())
print('--------------------------------------------------------------')
print(df.isnull().sum())
print('--------------------------------------------------------------')
print(df.nunique())
print('--------------------------------------------------------------')
print(df.sort_values(by='2022 Population',ascending=False).head(10))
print('--------------------------------------------------------------')

# not working
# print(df.corr())
# sns.heatmap(df.corr(),annot=True)
# plt.show()

df3=(df.groupby('Continent')[['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']].max().sort_values(by='2022 Population',ascending=False))
print(df3) 
print('--------------------------------------------------------------')
df2=df[df['Continent'].str.contains('Oceania')]
print(df2)
print('--------------------------------------------------------------')

# to convert index into columns and columns into index is done by using tranpose function
df1=df3.transpose()
print(df1)
# now we have to plot this df1 data
df3.plot(kind='bar')
plt.show()
# df1.plot(kind='bar')
# plt.show()

df.boxplot()
plt.show()
print('--------------------------------------------------------------')
print(df.dtypes)
print('--------------------------------------------------------------')
print(df.select_dtypes(include='float'))