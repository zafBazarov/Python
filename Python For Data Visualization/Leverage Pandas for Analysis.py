# Leverage Pandas for Analysis. 

# We will learn loading sample data, basic operations, data filtiring and so on using Pandas library. 

# Load CSV File

# Load car loan data from a scv file
import pandas as pd

df = pd.read_csv('car_financing.csv')
print(df)

# Load car loan data from an excel file
import pandas as pd

df = pd.read_excel('car_financing.xlsx')
print(df)


# If we want to know more about these commands we can use help() function
help(pd.read_excel)
                 
