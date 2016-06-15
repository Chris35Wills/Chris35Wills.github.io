---
---

# The numpy array

The main object of the numpy module is the multidimensional array - these are similar to the lists that are introduced on the [intermediate python course](../../Intermediate_python/lists) however, the contents of a numpy array must be all of the same type. Any given numpy array can be be of a number of dimensions - dimensions in numpy speak are called *axes*. Before you try using numpy, make sure you have imported it - ```import numpy```

## Array creation

An array can be created using a standard python list:

```python
a = numpy.array([1, 4, 5, 8], float)
```

Notice how we use numpy's array function and also specify the object type (in this case *float*). By typing ```a``` straight into the command line, you will now be presented with:

	>> a
	>> array([ 1.,  4.,  5.,  8.])

You can also use the ```print()``` function:

	>> print(a)
	>> [1.,  4.,  5.,  8.]

It isn't necessary to create arrays only by passing in lists - you can use the [numpy.arange()](http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.arange.html) function:

```python
x=numpy.arange(6)
```

or

```python
x=numpy.arange(1,10,1)
```

Notice the output from this second example - is this what you expected? If not, have a look at the documention for numpy.arange() (see [here](../numpy_import) if you can't remember how).

Two other useful functions for array creation include [numpy.ones()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.ones.html) and [numpy.zeros()](http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.zeros.html):

For example, a *1-dimensional* array of ones can be created using:

```python
b = numpy.ones(6)
```
.... and of zeros using:

```python
b = numpy.zeros(6)
```

## Multiple dimensions (or *axes*)

So far we have just dealt with single dimensions, however numpy can hold multiple. Using the same functions as introduced above, we can create a *2-dimensional* 2 x 5 array of ones using:

```python
a_2d=numpy.ones((2,5))
```

Print the variable ```a_2d``` out to the command line - are the dimensions as you expected? The saying *across the hall and up the stairs* doesn't hold here, with the first dimension specified being associated with the rows and the second dimension being associated with the columns of the new array. Try not to forget this - be sure that it will crop up again in the future!

## Creating arrays of random numbers

Numpy also offers a function to quickly create arrays of random numbers - the functions to do this are held within a sub-routine of numpy called [random](http://docs.scipy.org/doc/numpy-1.10.0/reference/routines.random.html). To create a *1-dimensional* array of random values:

```python
rand=numpy.random.random(7)
```

A *2-dimensional* array can be created as before:

```python
rand_2d=numpy.random.random((4,4))
```

You will notice that the values are between 0 and 1. Have a look at [the documentation](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.random.random.html) for creating random arrays between different limits.

# Exercises

* Create a *1-dimensional* array of ones 
* Create a *2-dimensional* array of random numbers 
* Create a 10 x 10 *2-dimensional* numpy array of ones of float type
* Create a 10 x 10 *2-dimensional* numpy array of zeros of integer type

... solutions can be found [here](../numpy_array_answers)

# [Previous](../numpy_import) [Home](../README_numpy) [Next](../numpy_array_funcs)