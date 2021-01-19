#install pandas using Pip this will install numpy as well
# pip3 install pandas
import pandas as pd
import numpy as np

#importing data from various sources Csv, excel, sql.
df = pd.read_csv('Example.csv', delimiter= ',')
#df = pd.read_excel('Example.xlsx', 'Sheet1')
# set your variables for for username, pwd, database  in below sql connection string
# sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#sql_connection =
#query = "Select * from Test_Table where Status = '1'

#df = pd.read_sql(query, sql_connection)

#Accessing data by column names or positionally
print(df.head(5)) # print all columns only first 5 rows
print(df.tail(5)) # print all columns only last 5 rows
print(df.shape) # print number of rows and columns in dataframe
print(df.columns) #print column names
print(df[0:].head(5)) #print first column first 5 values by column position
print(df['Office'].head(5)) #print same column first five values by column name
df2 = df[0:2]  ## only take the first 2 columns positionally
print(df2.columns)
df3 = df[['FirstName', 'LastName', 'Email']] # only take 3 columns by name
print(df3.columns)

##setting column type
df['Year'] = df['Year'].astype(int) # sets column as interger
df['Office'] = df['Office'].astype(str) # sets column to string
df['LastUpdated'] = pd.to_datetime(df['LastUpdated']) # sets column to Datetime

#some basic filtering/manipulation of data
df['FirstName'] = df["FirstName"].str.title()
print(df['FirstName'])
df[df['FirstName']] = df["FirstName"].str.upper()
print(df['FirstName'])
df['Email'] = df["Email"].str.lower()
print(df['Email'])

new = df["Email"].str.split("@", n = 1, expand = True) # splits string at the @ for one split next two lines create 2 columns that use the pieces.
df["user"]= new[0]
df["domain"]= new[1]

df['col'] = df['Office'].str[:3] # creates a new column grabbing the first 3 positions of Office column
df = df[df['Year'] != 0] # Only keep rows that have a FieldName value not equal to zero

# fills the NaN values that pandas will assign null values on import.
df['Year'] = df['Year'].fillna(0)

filter = 2015
data = []
# for loop to iterate over all rows in the frame, there are better ways to do this..
for index, row in df.iterrows():
    if row['Year'] > filter:
        data.append(row)  ## appends rows to series that meet row criteria above
    elif row['Year'] == 0:
        data.append(row)
df2 = pd.DataFrame(data, columns=['FirstName', 'LastName', 'Email', 'Office', 'LastUpdated', 'col'
                                  'domain', 'user'])

# Setting a column based on other data in the Dataframe
conditions = [
    (df['col'] == 'none'),
    (df['col'] == '123'),
    (df['Office'] == '134') & (df['Email'] == 'none@none.com'), #example 2 column condition
    (df['LastName'] == 'Smith'),
    (df['domain'] == 'example.com') & (df['FirstName'] == 'John')]

choices = ['No Office', 'Value2', 'Value3', 'Value4', 'Value5']
df['Status'] = np.select(conditions, choices, default='New')
print(df)



























