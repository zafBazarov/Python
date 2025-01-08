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
With a pandas, we can select rows using slicing like this: series[start_index:end_index}
The end_index is not inclusive. This behavior is very simple to Python lists.

# printing a special column
  df['car_type']

# slicing a column up 10 rows
df['car_type'][0:10]

# Selecting Columns using ``loc``
The pandas attribute .loc allow you to select columns, index, and slice your data.

# pandas dataframe
df.loc[:, ['car_type']].head

#pandas series
df.loc[:, 'car_type'].head


## Filter and Clean data

# Let's firts start by looking at the car_type column
# pandas dataframe
df['car_type'].value_counts()

# Notice that the filter produces a pandas series of True and False values
car_filter = df['car_type']=='Toyota Sienna'
car_filter

# Approach 1 using square brackets
# Filter dataframe to get a DataFrame of only 'Toyota Sienna'
df[car_filter].head()

# Approach 2 using .loc
# Filter dataframe to get a DataFrame of only 'Toyota Sienna'
df.loc[car_filter, :]

# Notice that it looks like nothing changed
# This is because we did not update the dataframe after applying the filter
df['car_type'].value_counts()

# Filter dataframe to get a DataFrame of only 'Toyota Sienna'
df = df.loc[car_filter, :]

df['car_type'].value_counts()

# interest_rate Filter

df['interest_rate'].value_counts()

# Notice that the filter produces a pandas series of True and False values
df['interest_rate']==0.0702

interest_filter = df['interest_rate']==0.0702
df=df.loc[interest_filter, :]
df['interest_rate'].value_counts(dropna=False)

# Combining Filters
 we know join car_filter and interest_filter filtesr. 
& = and, | = or,^ ) exclusive or, ~ = not
df.loc[car_filter & interest_filter, :]

## Renaming and deleting Columns
It is often the case where you change your column names or remove unnecessary columns. 

***Rename columns***

Here are two popular ways to rename dataframe columns. 
1. ***dictionary substitution***. very useful if you only want to rename a few of the columns.
2. ***list replacement***: requires a full list of names (this is more error prone)

# This wont work as there is a spcae in the column name
# I want to fix that
df.['Principal Paid']

# Approach 1 dictionary substitution using rename method
df = df.rename(columns = {'Starting Balance': 'starting_balance',
                          'Interest Paid': 'interest_paid',
                          'Principal Paid': 'principal_paid',
                          'New Balance': 'new_balance'}
              )

# Approach 2 list replacement
# Only changing Month -> month, but we need to list the rest of columns
df.columns = ['month',
              'starting_balance',
              'Repayment',
              'interest_paid',
              'principal_paid',
              'new_balance',
              'term',
              'interest_rate',
              'car_type']

## Deleting columns

# Approach 1
# This approach allows yu to drop multiple columns at a time
df = df.drop(columns=['term'])
df.head()

# Approach 2 use the del command
del df['Repayment']
df.head()

