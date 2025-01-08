# Leverage Pandas for Analysis. 

# We will learn loading sample data, basic operations, data filtiring and so on using Pandas library. 

# Loading a dataset

# Load car loan data from a scv file
import pandas as pd

df = pd.read_csv('car_financing.csv')
print(df)

# Load car loan data from an excel file
import pandas as pd

df = pd.read_excel('car_financing.xlsx')
print(df)

# 

# If we want to know more about these commands we can use help() function
help(pd.read_excel)

# There are many different file types you can load than just CSV and Excel files into Pandas DateFrames. If you're curious about what other kind of files you can load, I encourage you to do pd.read_ to see what other kind of files you can load. 

## Basic Operations
1. Assure that you have correctly loaded the data
2. See what kind of data you have
3. Check the validity of your data

# Viewing the first and last 5 rows

# Select top N number of records (default = 5)
df.head()

# Select bottom N number of records (default = 5)
df.tail()

# Check the column data types using the dtypes attribute
df.dtypes

# Use the shape attribute to get the number of rows and columns in your dataframe
df.shape()

# The infor method gives the column datatype + number of non-null values
# Notice that we seem to have 405 non-null values for all but the Interest Paid column.
df.info()
