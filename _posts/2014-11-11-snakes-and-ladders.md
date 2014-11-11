---
layout: post
title: Snakes and ladders - rows and cols in Python
categories: Python
tags: python, image, array
---

Every time I have to work with rows and columns I always mix this up - it must be 
because of the "across the hall and up the stairs" phrase I remember from school 
geography lessons. 

When dealing with arrays and looking at their shape, python will always report the 
rows first and then the columns. You can think of this howver you like (i,j) or 
(x,y) or (rows,cols). Whatever your preference, j, y or cols come first followed 
by j or x or rows.

{% highlight python %}
In [113]: image_array.shape
Out[113]: (11000, 6000)

# Image is 11000 rows by 6000 columns
{% endhighlight %}

Python goes down the stairs and across the hall - perhaps this is the result of 
the serpentine link to snakes and ladders - the snake wantsa you to slip back down 
to the beginning as opposed to going across and up a ladder... alas, I digress.

