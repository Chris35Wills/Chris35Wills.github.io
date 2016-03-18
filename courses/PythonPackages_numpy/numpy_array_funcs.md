---
---

# Array functions

Each time we created an array in the above examples, we have created a new numpy array *object* (if you are unfamiliar with objects, they are covered in the [intermediate course](../../Intermediate_python/objects)). The key thing to take away here is that by creating a new array object, you now have access to various methods associated with it... let's look at some examples.

For any given array, a useful metric to access would be its size - this is achieved using the ```shape``` method. First, create an array of ones (e.g. ```b = numpy.zeros(6)```), and then type:

```python
b.shape
```

and you should see the following printed out:

	>> (6L,)

For a *2-dimensional* array (create using ```a_2d=numpy.ones((2,5))```):

```python
a_2d.shape
```

and you should see the following printed out:

	>> (2L, 5L)

To see what other methods are available, just type the name of an existing array followed by a full stop - e.g. ```your_array.``` and hit tab and you will see a number of additional functions. Remember that to find out more information about how to use a specific function, just type ```help(your_array.function)``` or ```your_array.function?```. 

Useful array specific functions include: max, min, mean, sum, dtype and copy amongst others. Have a look at the documentation - the more aware you are of what is available, the more that you'll be able to take advantage of python and its associated packages.

```reshape``` is a particularly useful function if you want, for example, to create an array of specific values of specific dimensions - let's create a 2-dimensional array with values between 0 and 9:

```python
arr=numpy.arange(0,10)     # create a simple array of numbers in 1D
arr.reshape(2,5)         
```

After firstly creating a simple *1-dimensional* array, using the array function ```reshape``` and by specifying your desired dimensions (make sure they work by considering the length of the array you are manipulating), you will have seen your array restructured. However, despite this, the shape of variable ```arr``` will still be as it was before the reshape function call. To keep the array in the new shape, you must assign it to a new variable:

````python
arr_2d=arr.reshape(2,5) 
```

# Exercises

* Create a *1-dimensional* array of ones and print out its shape
* Create a *2-dimensional* array of random numbers and print out its shape
* Create a *2-dimensional* array of values between 10 and 30 and print out its shape
* Create a 10 x 10 *2-dimensional* numpy array of random numbers - what are the max, min and mean values of this array?

... solutions can be found [here](../numpy_array_funcs_answers)

# [Previous](../numpy_array) [Home](../README_numpy) [Next](../numpy_indexing)