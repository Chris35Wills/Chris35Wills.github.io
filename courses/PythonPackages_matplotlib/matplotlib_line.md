---
---

# Your first plot

Matplotlib contains a module called ```pyplot``` which enavbles MATLAB style plotting and customisation. We will be using this throughout this mini-course. Now, in a new terminal type the following:

```python
import matplotlib.pyplot as plt
```

If you have never imported a module before, take a look [here](../matplotlib_install). Something slightly different about the above command is the addition of *as plt* - all this does is enables you to access everything in ```matplotlib.pyplot``` by just typing ```plt``` i.e. instead of typing ```matplotlib.pyplot.function``` each time, all we have to now type is ```plt.function``` which is both quicker and tidier (which makes for easier reading).


Let's start by creating some new data which we'll do using [numpy](http://www.numpy.org/) (see [here](../../PythonPackages_numpy/README_numpy) if you haven't used numpy before) - in a new terminal, type the following:

```python
import numpy as np
data=np.array((np.arange(0,10,1), np.arange(0,30,3)))
```

## A basic line plot

To create a line plot, we will use matplotlib's ```plot()``` function (remember you can find out how to use it by typing ```plt.plot?```). We need to pass in our data - type the following to create the basic line plot:

```
plt.plot(data[0,:],data[1,:])
plt.show()
```

