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



## Aggreaget functions

# sum the values in a column
# total amount of interest paid over the course of the loan
df['interes_paid'].sum()

# sum all the values across all columns
df.sum()

# NOtice that by default it seems like the sum function ignores missing values.
help(df['interest_paid'].sum)

# The info method gives the column datatypes + number of nun-null values
# Notice that we seem to have 60 non-null values for all but the Interest paid column
df.info()


## Identify missing data
When working with a dataset we will often run into missing values

***Missing Data***
  - Hint at data collection errors
  - Indicate improper conversion or manipulation
  - Not actually be considered missing

***Missing Data*** may be listed: 
- Zero
- False
- Not applicable
- Entered an empty string

***Before you can graph data, you need to make sure there are no missing values***

# Finding Missing Values
df.info

Two common methods to indicate where values in a DataFrame are missing are ``isna`` and ``isnull``. They are exactly the same methods, but with different names. 
The reason why this is the case is in the R language, NA and null are two different things. This is to make our programmers have an easier time when working with Python. I tend to prefer isna as this tends to be similar in naming to other Python methods.

As you see it in the code over here I have the Panda Series interest_paid. I'm using the isna method, and what this does is this is producing a Panda Series of true and false values. It'll be true where I have a NaN value, and it'll be false where I don't.

# Notice wew have a Pandas Series of True and False values
df['interest_paid'].isna().head()

The next thing I'm doing is I'm assigning this true and false filter to the variable interest_missing. And the reason why I'm doing this is I want to take that filter and eventually use it to isolate my missing data. 
What the code here is doing is I want to look at the row where I have the missing values. 

# Filtiring based on misssing values
interest_missing = df['interest_paid'].isna()

# Looks at the row that contains NaN for interest_paid
df.loc[interest_missing]

And what you see here is I have a missing value in the interest paid column. This will be a problem for later. 

It's important to keep in mind, that you can also use the knot operator to negate the filter so that every row that's returned doesn't have a NaN. And as you see in the Pandas DataFrame, the row with index 35 is no longer here. 

# Keep in mind that we can use the not operator (~) to negate the filter
# every row that doesn't have a nan is returned.
df.loc[~interest_missing,:]

It's important to note, you'll often see code similar to what you see here.What we have is that same Pandas filter of true and false values. And then after, you have the aggregate function sum, which then sums all the true and false values to produce a result. The reason why this works is in Python, Boolean are a subtype of integer where true are ones and falses are zero.  

# The code counts the number of missing values
# sum() works because Booleans are a subtype of integers.
df['interest_paid'].isna().sum()


When working with a dataset, it's important to identify your missing values, as missing values can cause data misinterpretation errors, or even cause you an error when you try to graph your data.

# Remove or fill the missing data

It's really important to either remove that data or fill in the missing data with a reasonable value. This is a really important subject, as before you can graph data, you need to make sure you aren't trying to graph some missing values, as that can cause an error or cause a misinterpretation of the data. 

We're working with the car loan dataset and the first thing we're going to do is we're going to utilize the info method. And what the info method does is it shows us how many missing values we have in each of our columns. 

# identifying missing values
df.info()

And as you see, we have 60 non-null values for every column except for the interest paid column. This means that we have one null value. 

There are a couple different ways to deal with missing data. The first way is simply to remove the missing values. And in pandas you can remove the missing values by using the drop NA method. And what the code here does is I have a pandas data frame from index 30 up until, but not including index 40, and I'm dropping the rows where I have any NAN values. And as you see here, I don't have a row at index 35 because I had a NAN value here. 

# Remove Missing Values

# You can drop entire rows if they contain 'any' NaNs in them or 'all'
# this may not be the best strategy for our dataset
df[30:40].dropna(how = 'any')

#Filling in Missing Values
The other way to deal with missing values is simply to fill them in and there are a variety of ways to fill in missing values. 

The first thing we're going to do is we're going to look at where the missing data is located by using a pandas series and then slicing it to look at indexes 30 up until, but not including index 40. As you see here, I have a NAN at index 35. 

# Looking at where missing data is located
df['interest_paid'][30:40]

The first thing we're going to try is we're going to try to fill the NAN with a zero by using the fill NA method. The reason why filling in a NAN with a zero is often not a good idea, is originally the NAN could have been something else. A zero could help you misinterpret the data. It's just one option. 

# Filling in the NaaN with a zero is probably a bad idea
df['interest_paid'][30:40].fillna(0)

The other method we could use is to fill in with a ***backfill***. And the way this works is perhaps better to show you. Where at Index 35, before I had a zero or a NAN, now I have an 89.77. This is because the index after it was an 89.77. This is very commonly done with ***time series data*** when you have a missing value. 

# back fill in value
df['interest_paid'][30:40].fillna(method = 'bfill')

Another way is to ***forward fill*** in your value. And this is also done with ***time series data***. 

# forward fill in value
df['interest_paid'][30:40].fillna(method = 'ffill')

``The difference between backfill and forward fill is backfill takes the value after the missing value and inserts it at the value that's missing. ``

``And what forward fill does is it takes the value before the missing value and inserts it where the missing value is. ``

***The reason why you use one versus the other is really dependent on your domain knowledge and your application. This is also a current area of research. It's called data imputation. ***

Another way to fill in missing values is through ***linear interpolation***. And what this does is it uses a linear model to fill in the missing value. And as you see here, this 93 is between the 96 and the 89. 

# linear interpolation (filling in NaN of values)
df['interest_paid'][30:40].interpolate(method = 'linear')

What the code here is doing is I'm finding the total interest paid over the course of a loan by using the sum method. And I should note, the sum method doesn't account for NANs. And as you see here, this is the total amount of money paid toward interest over the course of a loan. It's important to keep in mind that the sum method by default ignores NANs. 

# Interest paid before filling in the NaN with a value
df['interest_paid'].sum()

So after we fill in the NAN value with a real value, this might change. What the code here is doing is this is producing a Boolean array of true and false values where I'll have a true value where I have a NAN and a false value where I don't, and I'm assigning it to the variable interest_missing. From there, I'm utilizing the LOC operator and filling in that missing N value with the value 93.24. 

# Fill in with the actual value
interest_missing = df['interest_paid'].isna()
df.loc[interest_missing, 'interest_paid'] = 93.24

Now, when I sum over the entire column, I'll get a different number. This is perhaps more accurate, and I should note the value of removing or filling in your data is that oftentimes you get more accurate calculations. 

# Interest paid before filling in the NaN with a value
df['interest_paid'].sum()

In this case, the reason why I filled in the value with 93.24 is because I knew what the actual value should have been. This is due to my domain knowledge of loans. For whatever application you're working with, it's often best to try to get the most accurate value to fill in for your missing values. 

And as you can see here, we don't have NAN values in the data frame anymore. 

# Notice we dont have NaN values in the DataFrame anymore
df.info()

Once you've identified your missing values, removing them or filling them in often gives you more accurate calculations and makes the results more interpretable.

# Convert pandas DataFrames

When working with Pandas DataFrames, you'll oftentimes find you want to convert them to NumPy arrays or Python dictionaries. ``The reason why is because certain libraries prefer NumPy rays or Python dictionaries as inputs to their methods as opposed to Pandas DataFrames.``

In this video, we'll work with the car loan dataset again, and we're going to look at the first five rows. There are two ways to convert Pandas DataFrames to NumPy arrays. 

df.head()

***Convert Pandaas DataFrames to NumPy arrays***
The first approach is to use the two underscore NumPy method, and what this outputs is a NumPy array. 

# Approach 1 
df.to_numpy()

The second approach is to use the values attribute, and this also produces a NumPy array. I should note that either of these approaches works just as well as the other. 

#Approach 2
df.values

***Convert Pandaas DataFrames to Dictionaries***

You can also convert Pandas DataFrames to Python dictionaries. You can do this by using the two underscore dict method, and the reason why you'd want to do this versus convert your Pandas DataFrame to a NumPy array is oftentimes you're interested in preserving the indices of your Pandas DataFrame. 

df.to_dict()

``The practicality of this is that sometimes certain libraries don't accept Pandas DataFrames as inputs to their methods.``


