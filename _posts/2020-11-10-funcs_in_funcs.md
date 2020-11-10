---
layout: post
title: Functions in functions with varying numbers of arguments
categories: python
---

Developing a moving window operation framework to work on large numpy arrays (of digital elevation models), I need to modify one "master" moving window function to take in additional functions for which the number of variables might vary. 

This master function creates a kernel which moves across the array, each movement instance returning a kernel (e.g. 3x3) of values.

To this master function, each time it gets a new kernel of values, I want a specific function to be run. To do this, I want to therefore pass any type of kernel operating function. Given that for this application, the values per kernel are of topographic elevations, the functions might for example be used to calculate surface slope or aspect. The different functions doing these derivative calculations may need a varying number f arguments - so my question is - how do I pass one function with specific parameters to another existing function?

Some handy help [here](https://stackoverflow.com/questions/803616/passing-functions-with-arguments-to-another-function-in-python) answered my question.

Here's an example:

```python
from functools import partial

def performer(f):
	f()

def func1(a,b):
	print(a+b)

def func2(a,b,c):
	print((a*b)/c)

def func3(a,b, c, div=10):
	print((a+b)*c/div)


performer(partial(func1,2,2))
performer(partial(func2,2,2,3))
performer(partial(func3,2,2,3))
```

Where `performer()` represents my master windowing function, `func1()`, `func2()` and `func3()` can then represent whatever it is I want to run inside `performer()`. `functools.partial` let's me pass different numbers of arguments as required.

Below shows an example of where you need to pass something to the function from inside the master function:

```python
import numpy as np

def master_func(f):
	arr=np.ones((3,3))	
	print(f(arr))

def multiplier(v,arr):
	return(arr*v)

arr_doubler=partial(multiplier,2)
master_func(arr_doubler)
```

Below shows an example of where you need to pass something to the function from inside the master function, but also where the function being passed to master has some optional arguments. Therefore, you must pay attention to the order of arguments being passed using `partial`:

```python
def multiplier_2(v,arr,a=2):
	return((arr*v)/a)

arr_doubler_2=partial(multiplier_2,2,a=3)
master_func(arr_doubler_2)
```