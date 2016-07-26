---
layout: post
title: Apply function over Pandas dataframe
categories: python, pandas
tags: python pandas
---

The [assign](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.assign.html) function available in [Pandas](http://pandas.pydata.org/) is extremely convenient and allows for quick calculations across a dataframe. I need to make more use of this. You create your dataframe such as:

```python
import pandas as pd
import numpy as np

x=np.arange(0,100,1)
y=np.arange(0,100,1)

index=np.arange(0, len(x), 1)
columns=['x','y']
df=pd.DataFrame(index=index, columns=columns)

df['x']=x
df['y']=y
```

You can then use the assign function, where here we use it to create a new column calculating distance between successive xy pairs using the function [rolling_apply](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.rolling_apply.html), the x and y values being held in separate columns:

```python 
df=df.assign(x_diff=pd.rolling_apply(df['x'], 2, \
  lambda x : x[1]-x[0])) 

df=df.assign(y_diff=pd.rolling_apply(df['y'], 2, \
  lambda y : y[1]-y[0]))

df['distance']=np.hypot(df['y_diff'], df['x_diff'])
```

You can then manipulate the result as required:

```python
np.cumsum(df['distance']).plot()
plt.title("Cumulative distance")
plt.show()
``` 

![Cumulative distance]({{ site.baseurl }}/images/cumulative_distance.png)	
