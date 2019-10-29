---
layout: post
title: Applying a function to all rows of a column with pandas
categories: Python
---

A common operation to implement with a pandas dataframe is to run a function for each entry or row of a column.
Below shows how we can do this using a simple custom function.

First we'll put together a dataframe - remember that you could read your own in from file using for example `pandas.read_csv()` - incidentally, we'll need to import `pandas` and, just for this example, `numpy` too:

{% highlight python %}
	import pandas as pd
	import numpy as np

	# Create a dataframe with a dictionary (could just read one in too)
	input_data={'var1':np.random.randint(low=-50, high=50, size=10),
				'var2':np.random.randint(low=-50, high=50, size=10)}
	data=pd.DataFrame(data=input_data)

	# Have a look at the data frame you've created
	data.head()
{% endhighlight %}

Now let's make the function that we want to apply to each entry of a specified column:

{% highlight python %}
	# Create a function to apply to each row of the data frame
	def negative_clean_up(value):
		"""Converts all negative values to positive and divides by 2
		"""
		if value<0:
			return(abs(value)/2)
		else:
			return(value)
{% endhighlight %}

The final step is to apply the function to a specific column - remember that to save the changes to the dataframe variable, you'll need to assign it (i.e. column name = whatever...). Rather than writing a loop that goes through each row, the function `pandas.DataFrame.apply()` will do all of the work for us:

{% highlight python %}
	# Apply that function to every row of the column
	data['var1']=data['var1'].apply(negative_clean_up)

	# Check the data output
	data.head()
{% endhighlight %}

If you want to apply it to all columns, you can use the function `applymap()`:

{% highlight python %}
	data.applymap(lambda x: negative_clean_up(x))
{% endhighlight %}

To read more about the `lambda` function, have a read [here](https://www.w3schools.com/python/python_lambda.asp).










