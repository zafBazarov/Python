# Create heatmaps

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
