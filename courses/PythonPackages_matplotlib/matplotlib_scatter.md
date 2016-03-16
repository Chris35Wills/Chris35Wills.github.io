---
---

# Your first scatter plot

Matplotlib contains another module called ```pyplot``` which enavbles MATLAB style plotting and customisation. We will be using this throughout this mini-course. Now, in a new terminal type the following:

```python
import matplotlib.pyplot as plt
```

If you have never imported a module before, take a look [here](../matplotlib_install). Something slightly different about the above command is the addition of *as plt* - all this does is enables you to access everything in ```matplotlib.pyplot``` by just typing ```plt``` i.e. instead of typing ```matplotlib.pyplot.function``` each time, all we have to now type is ```plt.function``` which is both quicker and tidier (which makes for easier reading).

We are also going to need some data so now type:

```python
import numpy as np
```

Now lets create some random point data to mimic some xy coordinates and some associated attribute:

```python
xyz=np.array(np.random.random((100,3)))
```

To create out plot, we need to access the ```plt.scatter()``` function (remember to check out the function help by using ```plt.scatter?```). This function takes in 2 variables to plot - we'll use the first 2 columns of our ```xyz``` array:

```python
plt.scatter(xyz[:,0], xyz[:,1])
```

You should see something like the following being printed out:

	>>> <matplotlib.collections.PathCollection at 0x1afd1d30>

To view the image, we can use the function ```plt.show()``` - type this in:L

```python
plt.show()
```

and you should see something like this:

!["Your first matplotlib scatter plot"]({{ site.baseurl }}../first_scatter.png)

This is all well and good but we are missing some important components - for example axis labels and a title. These are easily added - first you must re-create the scatter plot:

```python
plt.scatter(xyz[:,0], xyz[:,1])
```

and now we can add some labels:

```python
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
```

If you run ```plt.show()``` again, things will be starting to look better. If you've had a look at the documentation for ```plt.scatter()``` you will also see that the function can take in a scalar to adjust the marker size (starts at a default value of 20) - let's make these a bit smaller:

```python
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size)
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
plt.show()
```

What we can also do is change the colour of the points - want them in red? Then when invoking ```plt.scatter()```, you'll need to set the ```c``` flag (more info on colours can be found [here](http://matplotlib.org/api/colors_api.html)):

```python
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size, c='r')
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
plt.show()
```

Something else that can be handy is to colour the points by another variable - in the case of our ```xyz``` test data, currently we are only using the first 2 columns - lets use the third colmn to colour the plot:

```python
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size, c=xyz[:,2])
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
plt.show()
```

By adding these new colours, we now have information on the plot that alone is not particularly informative - we need a colourbar and fortunately, there is a method for creating this - ```plt.colorbar()```:

```python
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size, c=xyz[:,2])
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
plt.colorbar()
plt.show()
```

Last but not least, lets add a title to the colorbar to indicate what it represents - there isn't a direct function for doing this like ```plt.colorbar_title()``` - instead, after creating your initial plot as above, assign the creation of your colorbar to a variable like this:

```python
cbar = plt.colorbar()
```
This creates a colorbar object, the methods of which you can now access - have a look by typing ```cbar.``` followed by the tab key.

To set the title, we need to type:

```python
cbar.set_label("elevation (m)")
```

You can change the distance the label is from the colorbar by using the labelpad option (positive moves away, negative moves it closer):

```python
cbar.set_label("elevation (m)", labelpad=-1)
```

Now, to create your final plot just type:

```python
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size, c=xyz[:,2])
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
cbar= plt.colorbar()
cbar.set_label("elevation (m)", labelpad=+1)
plt.show()
```

When you close the window that opens, type ```plt.clf()``` to clear everything.

# [Previous](../matplotlib_install) [Home](../README_matplotlib) [Next](../matplotlib_line)

