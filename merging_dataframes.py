import pandas as pd

df1=pd.read_csv(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output\LOTR.csv")
df2=pd.read_csv(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output\LOTR 2.csv")

print('--------------------------------------------------------------------------------------------------------------------------------')

print(df1)

print('--------------------------------------------------------------------------------------------------------------------------------')

print(df2)

print('--------------------------------------------------------------------------------------------------------------------------------')

# normal left join
print(df1.merge(df2))

print('--------------------------------------------------------------------------------------------------------------------------------')


# left join along with defining attributes
print(df1.merge(df2,how="inner",on='FellowshipID'))

print('--------------------------------------------------------------------------------------------------------------------------------')

print(df1.merge(df2,how="outer",on='FellowshipID'))

print('--------------------------------------------------------------------------------------------------------------------------------')

print(df1.merge(df2,how="right",on='FellowshipID'))

print('--------------------------------------------------------------------------------------------------------------------------------')

print(df1.merge(df2,how="left",on='FellowshipID'))

print('--------------------------------------------------------------------------------------------------------------------------------')


# concept of join similar to merge
print("Joining two dataframes using the concat function:")

print(df1.join(df2,on='FellowshipID',how='inner',lsuffix='_xxx',rsuffix='_yyy'))

print(pd.concat([df1,df2]))
