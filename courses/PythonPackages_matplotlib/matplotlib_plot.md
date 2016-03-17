---
---

# Your first plot

Matplotlib contains a module called ```pyplot``` which enables MATLAB style plotting and customisation. We will be using this throughout this mini-course. Now, in a new terminal type the following:

```python
import matplotlib.pyplot as plt
```

If you have never imported a module before, take a look [here](../matplotlib_install). Something slightly different about the above command is the addition of *as plt* - all this does is enables you to access everything in ```matplotlib.pyplot``` by just typing ```plt``` i.e. instead of typing ```matplotlib.pyplot.function``` each time, all we have to now type is ```plt.function``` which is both quicker and tidier (which makes for easier reading).

Let's start by creating some new data which we'll do using [numpy](http://www.numpy.org/) (see [here](../../PythonPackages_numpy/README_numpy) if you haven't used numpy before) - in a new terminal, type the following:

```python
import numpy as np
data=np.array([np.arange(0,10,1), np.arange(0,30,3)])
```

To make things more readable, lets assign this data to two separate variables:

```python
x=data[0,:]
y=data[1,:]
```

## A *basic* line plot

To create a line plot, we will use matplotlib's basic ```plot()``` function (remember you can find out how to use it by typing ```plt.plot?```). We need to pass in our data - type the following to create the basic line plot:

```
plt.plot(x,y)
plt.show()
```

You can change your line style by passing in a third argument - to create a dashed line type:

```
plt.plot(x,y, '--')
plt.show()
```

You can also change the colour - for a red dashed line:

```
plt.plot(x,y, 'r--')
plt.show()
```

There are lots of available options for modifying your marker style - look [here]() or check out the function help (```plt.plot?```)

## A *basic* scatter plot

Using the same points, we can use ```plt.plot()``` to create a simple scatter plot. Unlike the line plot (the default of ```plt.plot()```), we must specify the marker type, in the same way as we created a dashed line. For simple points, type the following:

```python
plt.plot(x,y, 'o')
plt.show()
```

To make the points red:

```python
plt.plot(x,y, 'ro')
plt.show()
```

To use a different symbol rather than a point (let's go for red stars):

```python
plt.plot(x,y, 'r*')
plt.show()
```

To make the points bigger, you must use the ```markersize``` option:

```python
plt.plot(x,y, 'r*', markersize=10)
plt.show()
```

You'll see that at the edge of the plot, some of the points exceed the axis and are hidden. We can adjust this by changing the plots extent by setting the x and y limits (```plt.xlim()`` and ```plt.ylim()``` respectively):

```python
plt.plot(x,y, 'r*', markersize=10)
plt.xlim(-1, 10)
plt.ylim(-1, 28)
plt.show()
```

We *hardwired*  the axis limit values above - this works but if you will be repeatedly changing the data being used for a plot, this can end up holding you back (and hard wiring is something to avoid where possible when programming as it can end up biting you back when a variable gets hidden away as you write longer scripts). We can instead dynamically set the limits based on what we know about our x and y data and we could instead just fix an offset value - let's say we want the axis to extend to 1 value greater than the maximum and minimum values in or x and y arrays i.e.:

```python
offset=1
plt.plot(x,y, 'r*', markersize=10)
plt.xlim(x.min()offset, x.max()+offset)
plt.ylim(y.min()offset, y.max()+offset)
plt.show()
```

Should you now change the values in the x and y arrays, you don't have to manually retype your extent values. 

# [Previous](../matplotlib_install) [Home](../README_matplotlib) [Next](../matplotlib_scatter)
