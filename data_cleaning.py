import pandas as pd

df=pd.read_excel(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output\Customer Call List.xlsx")

pd.set_option('display.max.columns',20)

# removing duplicates from data
df=df.drop_duplicates()
# print(df)

# deleting the columns that are not useful
df=df.drop(columns='Not_Useful_Column')
# print(df)


# removing extra symbols or characters from data
# df['Last_Name']=df['Last_Name'].str.strip('_')
# df['Last_Name']=df['Last_Name'].str.strip('...')
# df['Last_Name']=df['Last_Name'].str.strip('/')

# or.............or............or............or---------->

# above mentioned trick is for stripping the string one by one character by character
# but we can also do this by using all the desired strig in single string
df['Last_Name']=df['Last_Name'].str.strip('123.,/_')
# print(df)

# skipping replace function....
# using replace function to set data similar in each column
df['Phone_Number']=(df['Phone_Number'].str.replace('/',''))
df['Phone_Number']=(df['Phone_Number'].str.replace('-',''))
df['Phone_Number']=(df['Phone_Number'].str.replace('|',''))
df['Phone_Number']=(df['Phone_Number'].str.replace('Na',''))
df['Phone_Number']=(df['Phone_Number'].str.replace('NaN',''))
# print(df)

# split function is not working
# splitting function
# print(df['Address'].str.split(',',1,expand=True))
# print(df['Address'])

df['Paying Customer']=df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer']=df['Paying Customer'].str.replace('No','N')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')
# print(df)

df=df.replace('N/a','')
# now for removing removing empty data columns we will use fillna 
df=df.fillna('')
# print(df)

# now removing the data that has y in its do not call column
for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Y':
        df.drop(x,inplace=True)
   
# now removing the data that does not have phone number in column
for x in df.index:
    if df.loc[x,'Phone_Number']=='':
        df.drop(x,inplace=True)
# print(df)

df=df.reset_index(drop=True)
print(df)
 
df.to_excel(r"D:\BVP SSB\Data Analysis\Python\Files\Files For Output/Customer Call List After Cleaning.xlsx")

