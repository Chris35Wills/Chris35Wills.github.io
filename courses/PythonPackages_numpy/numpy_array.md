---
---

# The numpy array

The main object of the numpy module is the multidimensional array - these are similar to the lists that were introduced in the [introductory course]() however, the contents of a numpy array must be all of the same type. Anty given numpy array can be be of a number of dimensions - dimensions in numpy speak are called *axes*.

## Array creation

An array can be created using a standard python list e.g.

```python
a = numpy.array([1, 4, 5, 8], float)
```

Notice how we use numpy's array function and also specify the object type (in this case *float*). By typing ```a``` straight into the command line, you will now be presented with:

	In [6]: a
	Out[6]: array([ 1.,  4.,  5.,  8.])

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

So far we have just dealt with single dimensions, however numpy can hold multiple. Using the same functions as intriduced above, we can create a *2-dimensional* 2 x 5 array of ones using:

```python
a_2d=numpy.ones((2,5))
```

Print the variable ```a_2d``` out to the command line - are the dimensions as you expected? The saying *across the hall and up the stairs* doesn't hold here, with the first dimension specified being associated with the rows and the second dimension being associated with the columns of the new array. Try not to forget this - be sure that it will crop up again in the future!

## Creating arrays of random numbers

Numpy also offers a function to quickly create arrays of random numbers - the functions to do this are held within a subpackage of numpy called [random](http://docs.scipy.org/doc/numpy-1.10.0/reference/routines.random.html). To create a *1-dimensional* array of random values:

```python
arr_rand=numpy.random.random(7)
```

You will notice that the values are between 0 and 1. Have a look at [the documentation](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.random.random.html) for creating random arrays between different limits.

## Array functions

Each time we created an array in the above examples, we have created a new *numpy array object* (if you are unfamiliar with objects, they are covered in the [intermediate course](../../Intermediate_python/objects)) - the key thing to take away here is that by creating a new array object, you now have access to various methods associated with it... let's look at an example:

For any given array, a useful metric to access would be its size - this is achieved using the ```shape``` method - so for or *1-dimensional* zeros array, just type:

```python
b.shape
```

and you should see the following printed out:

	(6L,)

For the *2-dimensional* array:

```python
a_2d.shape
```

and you should see the following printed out:

	a_2d=numpy.ones((2,5))

To see what other methods are available, just type the name of an existing array followed by a full stop - e.g. ```a_2d.``` and hit tab and you will see a number of additional functions. Remember that to find out more information about how to use a specific function, just type ```help(a_2d.function)``` or ```a_2d.function?```. 

Useful array specific functions include: max, min, mean, sum, dtype and copy amongst others. Have a look at the documentation - the more aware you are of what is available, the more that you'll be able to take advantage of python and its associated packages.

# Exercises

* Create a *1-dimensional* array of ones and print out its shape
* Create a *2-dimensional* array of values from 1 to 11 
* Create a *2-dimensional* array of random numbers and print out its shape
* Create a 10 x 10 *2-dimensional* numpy array of ones of float type
* Create a 10 x 10 *2-dimensional* numpy array of zeros
* Create a 10 x 10 *2-dimensional* numpy array of random numbers - what are the max, min and mean values of this array?
