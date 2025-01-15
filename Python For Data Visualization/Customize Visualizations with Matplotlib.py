

# 1) Create heatmaps

We will learn how to create heatmaps using matplotlib and Seaborn, a matplotlib wrapper. So what is a heatmap? 

***Heatmap*** ``is a graphical representation of data where values are depicted by colors.`` 

Heatmaps allow you to easier spot where something happened and where it didn't. Consequently, what we choose for our color palette is important. Two types of color palettes are sequential, and this is appropriate when data ranges from relatively low values to relatively high values. There's qualitative, and this is best when you want to distinguish discrete chunks of data that do not have inherent ordering. 

``Heatmpa Colors``
- Sequential (low values to high values)
- Qualitative (discrete chunks of data)

To create a heatmap, we first have to import our libraries. We're going to make sure matplotlib is inline, which means that our graphics will display inline in the notebook. We're going to import NumPy as np, as well as Pandas as pd. To make a heatmap, we first have to import our libraries. We're importing matplotlib, seaborn, NumPy and Pandas. 

# The ``inline`` flag will use the appropriate backend to make figures appear inline in the not

%matplotlib inline

import numpy as np
import pandas as pd

# ``plt`is an alias for the `matplotlib.pyplot`` module
import matplotlib.pyplot as plt

# import seaborn library (wrapper of matplotlib)
import seaborn as sns

The data that we're going to load is the data from a confusion matrix, which is a table that is often used to describe the performance of a machine learning classification model. It tells you where your predictions went wrong. 

This particular table is derived from predicting labels for digits from zero to nine. For an understanding of the data, you can think of your columns as predictions for zero, for one, two, three, et cetera. You can think of your rows as their actual values. So this row would be actual value of zero, actual value of one, two, three, et cetera. So for this number, this is when we predicted a zero, and we predicted this 37 times, and the actual value was zero. For this column, this is when we predicted a one, and we predicted it correctly 39 times, because the actual value is one here. However, we have some misclassifications where we've made some bad predictions. In this case, three times we predicted an eight, when it was actually a one. 

# data


***Seaborn with Sequential Colormap***
To create a heatmap with Seaborn, you do .heatmap, you import your data. In this case, I want annotations, and you'll see what that looks like in a second. I'm specifying my color map. In this case, I'm choosing a sequential color map because my data ranges from relatively low values to relatively high values. I'm setting my X and Y labels, and here's our color map. 37 times we predicted a zero when it was actually a zero. 39 times we predicted a one when it was actually a one, but a couple times, we definitely did mess up, where we predicted a one when it was really an eight. This heatmap allows us to easily pick out our higher numbers, like this 51, from our lower numbers, like these zeros. This is because we have a sequential color palette. 

# sequential: appropriate when data ranges from relatively low
# (uninteresting values) to relatively high (interesting values).
plt.figure(figsize = (6,6))
sns.heatmap(confusion,
            annot=True,
            cmap = 'Blues');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');

***Seaborn with Qualitative Colormap***
The only difference with the code here from before is before, we had a sequential color map that was called blues. In this case, we have a qualitative color map, which is called ***pastel***. And as you see here, it's harder to determine which is a higher number based on color alone using this qualitative color map. 

# qualitative
plt.figure(figsize = (6,6))
sns.heatmap(confusion,
            annot=True,
            cmap = 'Pastell');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');

***Matplotlib***
It's important to keep in mind that you can also create a heatmap using pure matplotlib. This just happens to be a lot of code, and as you see the image, even though we had a lot of code, there's still other things that we could change to make it equal to our Seaborn color map. For example, the color here is black instead of white, which makes it harder to distinguish this 51 from this dark blue. 

#copy from original source
  
It's important to note what you choose for your color palette can make your visualization more or less interpretable. Additionally, sometimes it's easier to use a matplotlib wrapper like Seaborn, as it involves less code, and it's easier to make it aesthetically pleasing.

# 2) Histograms
We'll learn how to create histograms using Matplotlib. When first evaluating a dataset, ``it's a common practice to create histograms to explore your data, as it can give you a general idea of what your data looks like``. 

***Histogram*** is a summary of the variation in a measured variable. It shows the number of samples that occur in a category. A histogram is a type of frequency distribution. Histograms work by binning the entire range of values into a series of intervals and then counting how many values fall into each interval. While the intervals are often of equal size, they're not required to be. 

If you look at our import statements, we have Matplotlib inline. We're going to import pandas as pd, as not only can we manipulate data with pandas, we'll see how to create a histogram using the plotting functionality of the Pandas library. We're also going to import matplotlib.pyplot as plt. And even though we'll be creating a histogram through the plotting functionality of the Pandas library, you can always use base matplotlib to tune your figure. 

# The ``inline`` flag will use the appropriate backend to make figures appear inline in the not
%matplotlib inline

import pandas as pd

# ``plt`` is an alias for the ``matplotlib.pyplot`` module
import matlotlib.pyplot as plt

***Load Data***

The data that we'll use to demonstrate histograms is the house sales in King County USA dataset. We're going to load this data into a Pandas DataFrame by using pd.read_csv And as you can see, we have various features of a home in this data set. And what we'll be doing is visualizing a histogram of the price column. 

df =pd.read_csv('kingCountyHouseData.csv')

df.head()


***Histograms using Pandas***
To visualize, we can use the hist method. And as you can see, this is not very readable. 

df['price'].head()

# Using the default settings is not a good idea
# Keep in mind that visualization are an iterative process.
df['price'].hist()

One way to fix this is by rotating our x tick labels. To do this, we can do plt.xticks and specify that we want the rotation to be 90 degrees. And as you can see, we no longer have our x tick labels overlapping. 
# One solution is to rotate your xticklabels
plt.xtocks(rotation =90)

Alternatively, you could have changed the default plot style, as oftentimes, different plot styles have different defaults. And in this case, we're specifying the plot style to be seaborn. And as you can see, we don't have overlapping x tick labels. One problem with our current visualization is that we seem to have a lot of white space. This is most likely due to outliers. 

# If you want a quick solution to make the xtocklabels readable,
# try changing the plot style
plt.style.use('seaborn')

# Change the number of bins
# Seems better, but we still have empty spaces
df['price'].hist(bins =30)

Oftentimes, you're only interested in a subset of your data. Say for example, you're only interested in visualizing a subset of your data of homes under $3 million. To remove homes under $3 million, we're going to do df.loc and specifying that we want the price column and that we only want homes under $3 million. We're going to assign this Pandas series of true-false values to the variable price filter. From there, we can utilize our price filter by doing df.loc, inserting our filter of true and false values, specifying that we only want to look at the price column, and then creating a histogram off it. As you can see, we have less white space in our figure. 

# visualizing a subset of the data
price_filter = df.loc[:, 'price'] <= 3000000
df.loc[price_filter, 'price'].hist(bins =30)

One important thing to keep in mind is that data visualization is an iterative process, so there's always something else you can tune. Say, for example, I want to be able to distinguish my bars from each other. You can do this by specifying the edge color. In this case, I want to be black. As you can see here, I can now distinguish my bars from each other. You can also keep on tuning your graph to be more and more visually appealing. Just make sure that it's worth the effort.

# you can change the edgecolor and linewidth
price_filter = df.loc[:, 'price'] <= 3000000


df.loc[price_filter, 'price'].hist(bins =30,
                                    edgecolor ='black')
