---
layout: post
title: Install natgrid add on for matplotlib
categories: Python
tags: python matplotlib natbib
---

Trying to use the nearest neighbour interpolation routine through matplotlibs [griddata](http://matplotlib.org/api/mlab_api.html#matplotlib.mlab.griddata) function, I realised I needed to make use of the natgrid extension package. 

Working on windows and after as simple [a point and click approach as possible](http://stackoverflow.com/questions/28902724/install-natgrid-in-matplotlib-in-the-environment-of-python-2-7), I was able to find a build on this [site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#natgrid). 

Having never dealt with [.whl](https://pypi.python.org/pypi/wheel) files before I looked for some [help](https://pip.pypa.io/en/latest/user_guide.html#installing-from-wheels) and managed to install it very quickly using pip - something I've never needed to use as I've been able to stay within the packages directly available through the academic licensed version of [canopy](https://www.enthought.com/products/canopy/).

All I [ended up having to type](https://docs.python.org/3/installing/) (in the directory that I saved the .whle file from [earlier](http://www.lfd.uci.edu/~gohlke/pythonlibs/#natgrid)) was:

{% highlight python %}
python -m pip install .\natgrid-0.2.1-cp27-none-win_amd64.whl
{% endhighlight %}