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

# Simplify with slicing

# When working with large data sets often yoe are only interested in a smaller subset of your data.

## Slicing
1. How to select columns in pandas
2. How to use slicing operations in pandas

## Select columns using brackets
With square brackets, you can select on or mor columns. 

# Select one column using double brackets
df[['car_type']].head()

# Select multiple columns using double brackets
df[['car_type', 'Principal Paid']].head()

# This is a Pandas DataFrame
type(df[['car_type']].head())

# Select one column using single brackets
# This procedure a pandas series which is a one-dimensional array which can be labeled 
df['car_type'].head()

# Keep in mind that you can't select multiple columns using single brackets
# This will result in a KeyError
df['car_type', 'Principal Paid'].head()

## Pandas Slicing
With a pandas




