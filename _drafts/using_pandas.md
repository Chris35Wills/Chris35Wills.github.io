---
layout: post
title: Using pandas for reading in tab and csv type files
categories: Python
tags: python pandas
---

{% highlight python %}
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv("cresis_gridded.txt", sep = "\s*", header=None, names=["x","y","z","time"])
df = pd.read_csv("file.txt", sep = "\s*", 
	header=None, names=["x","y","z","time"])

x=df["x"].values
y=df["y"].values
z=df["z"].values
time=df["time"].values

data_line = df.iloc[0,:]
data_col = df.iloc[:,2]
{% endhighlight %}

#########################

---
layout: post
title: Install custom python libraries
categories: Python
tags: python function library module
---

You may have a number of functions that you frequently use and import in scripts your running. It's easy to install these functions so 
that you can install them without them being in the same directory as the main script you are running.

My base directory will be: "~/Github/", now copy the following:

1) create a folder in which you want to have your modules - lets call it 'fucntions' (this can contain subdirectories later on)
2) create a file called "__init__.py" - this will allow you to use pythons "import module" function at the top of a script
3) put your module containing all of your functions e.g. 'utils.py'

Your directory tree should now look something like this:

> ~/Github/functions/
		__init__.py
		utils.py

Next you need to enable python to find the module - for a specific python session you need to add the functions directory to the python path:

4) In a python window:

{% highlight python %}
import sys
sys.path ## prints out the current paths found in the pythonpath
sys.path.append('~/Github/functions/') ## adds the new directory to the python path
{% endhighlight %}

NB/ This is not a permanent addition - the next time you open up a python session, the function directory won;t be along the path. A permanent addition requires [an addition to be made to the PYTHPATH environment variable](https://docs.python.org/2/using/windows.html#excursus-setting-environment-variables).

5) Now assuming Python knows where your functions are, if want something from say the "utils.py" module you should be able to import like any other package:

{% highlight python %}
import utils
{% endhighlight %}

Assuming you've commented it appropriately, you can also take advantage of the help command:

{% highlight python %}
help(utils)
{% endhighlight %}

##############

