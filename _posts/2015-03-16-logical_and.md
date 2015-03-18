---
layout: post
title: Before I forget - logical_and from Numpy
categories: python
tags: python, numpy, logical_and
---

I keep coming back to needing this function, each time forgetting where to find it - populating an array based on conditions of other arrays which act as an input.

{% highlight python %}
> np.logical_and()
{% endhighlight %}  

# Example

{% highlight python %}
import numpy as np

# You have two arrays:

a = np.asarray([0,1,1,0,1,1,1,0])
b = np.asarray([2,3,5,1,6,7,3,8])

# Make another array which you'll later populate

c = np.zeros(a.shape) # array to be populatted using condition

# Populate c based on value conditions of arrays a and b

c[np.logical_and(a==1,b==3)] = 2 

{% endhighlight %}  
