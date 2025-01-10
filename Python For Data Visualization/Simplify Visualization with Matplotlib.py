
# 1) Basics of Matplotlib

We're going to learn about the Matplotlib library, which is ``a powerful tool capable of producing complex publication-quality figures with fine layout control in two or three dimensions.`` While this is an older library, so many libraries are built on top of it and use its syntax. The first thing we have to do is import the libraries we're going to use. We're going to utilize the pandas and NumPy libraries to manipulate data in a format that's suitable for plotting. We're going to import matplotlib.pyplot as PLT, and PLT is just an alias for the matplotlib.pyplot module. And lastly, we're going to import the seaborn library, which is a wrapper for Matplotlib as SNS. 

# The inline flag will use the appropriate backend to make figures appear inline in the notebook.
%matplotlib inline

import pandas as pd
import numpy as np

# ``plt`` is an alias for the ``matplotlib.pyplot`` module
import matplotlib.pyplot as plt

# import seaborn library (wrapper of matplotlib)
import seaborn as sns

***Load Data***

Before we can graph data, we have to have data in a form that's suitable for graphing. So we're first going to import the car loan data into a pandas data frame. 

# Load car loan data into a pandas dataframe from a csv file
filename = 'data/tabel1.csv'
df = pd.read_csv(filename)

We're next going to look at the first five rows of the data frame as this is a good practice. 

#View the first 5 rows of the dataframe
df.head()


Next we're going to check to make sure we don't have NANs in our data frame, as it is not easy to directly plot data that contains NANs. And to do this, we're going to use the info method. And as you can see, we have 60 entries in our data frame, and we have 60 non-null values for each column. 

#Checking to make sure we dont have NaNs in our dataframe
#It is not easy to directly plot data that contains NaNs
df.info()

We're going to graph month number on the X axis and interest paid and principle paid on the Y axis. But to first do that, we have to have our data in the form of NumPy array. And what this code over here does is I have my data frame, I'm using the LOC operator, I'm saying I want all the rows, and I just want the month column. So this is a panda series, and I'm turning this panda series into a NumPy array by using the values attribute and assigning this entire thing to the month number variable. And similarly, I'm doing the same for the interest paid column and the principle paid column.
month_number = df.loc[:, 'month'].values
interest_paid = df.loc[:, 'interest_paid'].values
principial_paid = df.loc[:, 'principial_paid'].values

month_number

Keep in mind, you can also check that the values attribute converts a column of values into a NumPy array by using the inbuilt ``type function``. 

# The values attribute converts a column values into a numpy array.
type(month_number)


*** ``plot`` method ***

Once you have data in an appropriate format, you can begin to plot it. In this case, we're going to plot month number on the X axis and principle paid on the Y axis. As a reminder, if you don't know what a method does, you can always use the inbuilt help function. 

help(plt.plot)


Now it is time for our first plot and we're going to do PLT.plot. And for our X axis we're going to have our month number. And for our Y axis, we're going to have our interest paid. And as you can see, it's not the prettiest plot. 

# Not the prettiest plot
plt.plot(month_number, interest_paid)
  
You can also plot another line on the same graph. So before we only graphed month number and interest paid, but we can also graph month number and principle paid. This is also not the prettiest plot. 

# You can also plot another line on the same graph
plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

***Choose Figure Style***

One way to make our plots more aesthetically pleasing is to choose a figure style. We'll use ``plt.style.available`` to select an appropriate aesthetic style for a figure. 

The default style is not the most aesthetically pleasing. On this line, I'm doing PLT.style.available and pressing shift enter to see the different styles I can choose from. 
# Our style choices
plt.style.available

The style of classic is very similar to what we've already plotted.  
# We are currently using default plot
# so this will not change much about our plot
plt.style.use('classic')

plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

However, the 538 style is more aesthetically pleasing. 
# fivethirtyeight style
plt.style.use('fivethirtyeight')

plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

If you're coming from R, you can also use the GG plot style as you can see here. 
#R Studio style
plt.style.use('ggplot')

plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

You can also use different styles like Tableau colorblind. 
#tableau style
plt.style.use('tableau-colorblind10')

plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

You can also use the seaboard style, which is a wrapper for Matplotlib, as you can see here. 
#seaborn style
plt.style.use('seaborn')

plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)

We've gone over how to use Matplotlib.plyplot to make line graphs. And we saw how when you change style, you can make your graphs more aesthetically pleasing.

_____
#2) Set marker type and colors

``Marker type``
  
  Here are a couple common marker types: 
+++++picture

In this graph we are graphing month number versus interested_paid and month number versus principial_paid. We put '.' marker and its size to 10. 

plt.style.use('seaborn')

plt.plot(month_number, interest_paid, marker = '.', marksize = 10)      # x=month_number, y=interest_paid, marker
plt.plot(month_number, principial_paid, marker = '.', marksize = 10)


``Change Color``

The ``c`` parameter accepts strings. Also parameter accepts hex strings. For instance, green is '#008000'. Additionally, we can use rgd tuples: 
++++++picture

# string color
plt.plot(month_number, interest_paid, c='k', marker = '.', marksize = 10)      # k = black color
plt.plot(month_number, principial_paid, c='b', marker = '.', marksize = 10)    # b = blue color

Keep in mind that this `c`` parameter also takes hex strings

# Using hex strings
# '#000000' is black
# '#0000FF' is blue
plt.plot(month_number, interest_paid, c='#000000', marker = '.', marksize = 10)      # k = black color
plt.plot(month_number, principial_paid, c='0000FF', marker = '.', marksize = 10)    # b = blue color

Keep in mind that this `c`` parameter also accepts rgb tuples
# Using rgb tuples
# (0, 0, 0) is black
# (0, 0, 1) is blue
plt.plot(month_number, interest_paid, c=(0, 0, 0), marker = '.', marksize = 10)      # k = black color
plt.plot(month_number, principial_paid, c=(0, 0, 1), marker = '.', marksize = 10)    # b = blue color

# 3) MATLAB-style vs. object syntax

A potentially confusing part of the Matplotlib library is that ``it has two different styles of syntax``. 

**MATLAB style**, this is a scripted interface designed to feel like MATLAB, where Matplotlib maintains a pointer to the current (active) figure and sends commands to it. 

***Object oriented syntax***, this is more often used in situations where you want more control over your figure. 

``Important note``: you can and often will have plots that will be created through a combination of the MATLAB style and the object-oriented style.`` 


**MATLAB style**
We'll start by looking at the MATLAB style syntax, and this typically starts by using the PLT plot command, where you have something in the x axis, you have something in the Y axis, and you have a bunch of parameters that you set. In this case, I'm setting the parameter C, which is color equal to K, which is the color black, and you can also have additional PLT dot plot commands to plot on top of the figure. And you can see the result here. 

# MATLAB style
plt.style.use('seaborn')

plt.plot(month_number, interest_paid, c='k')      # k = black color
plt.plot(month_number, principial_paid, c='b')    # b = blue color

***Object oriented syntax***
The object oriented syntax is as follows. You have PLT subplots. In this case, I just want one plot, so I'm making n rows equal to one and n columns equal to one, and this returns a topple. And I'm topple unpacking the figure and the axes. And then from there, I'm just doing axes plot what I want in the X axis, what I want in the Y axis, and additional other parameters. Similar to the MATLAB style syntax, you can also plot additional things on the same plot. 

# tuple unpacking
x, y = (3, 9)

# Object oriented syntax
fig, axes = plt.subplots (nrows = 1, ncols = 1)
axes.plot(month_number, interest_paid, c='k')      # k = black color
axes.plot(month_number, principial_paid, c='b')    # b = blue color

**Combination**
It's important to note that you can and often will see the MATLAB style and the object oriented style used together. So in this case, I have the object oriented style, I have the MATLAB style, and I have the object-oriented style, and it still produces the same plot. 

# Combination
fig, axes = plt.subplots (nrows = 1, ncols = 1)
plt.plot(month_number, interest_paid, c='k')      # k = black color
axes.plot(month_number, principial_paid, c='b')    # b = blue color


There are two separate styles of Matplotlib syntax. There's a MATLAB style and there's the object-oriented style, and that sometimes they're used in combination with each other.
