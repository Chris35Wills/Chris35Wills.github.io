---
---

# Importing matplotlib

If you are using a distribution of Python (e.g. [Anaconda](https://www.continuum.io/downloads) or [Canopy](https://www.enthought.com/products/canopy/)]), then matplotlib comes readily available.

In a python terminal, simply type the following:

```python
import matplotlib
```

Assuming this works, you should receive no error messages. If the module is not available then you'll need to have a look [here](http://matplotlib.org/users/installing.html).

The docs for matplotlib can be found [here](http://matplotlib.org/index.html).

# First time you've imported a module?

Modules are what make Python great - and there are plenty of them *freely* available. If ever there is something you think you need to code up from scratch, first have a look around to see if someone has already made a module that covers it - this saves you reinventing the wheel - you may be surprised to find that many of the things you'll want to do have already been worked out!

# Getting help on modules and functions

Each module available in python contains a variety of components including (functions)[http://www.learnpython.org/en/Functions]. To see what is available within a given module, module documentation can easily be found online - it is also possible to find a list of functions whilst you are on the Python command line. For example:

Following your initial statement - ```import matplotlib``` - now type ```matplotlib.``` and hit the tab key...

This will print out a list of the functions available within the matplotlib library. If there is a function you want to know more about, simply type ```help(matplotlib.function)``` or ```matplotlib.function?``` and the documentation will appear within your current terminal, usually offering a number of examples as how to make use of the function in question.

# [Previous](../README_matplotlib) [Home](../README_matplotlib) [Next](../numpy_array)