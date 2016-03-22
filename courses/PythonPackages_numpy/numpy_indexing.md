---
---

# Indexing and slicing

Indexing and slicing allow you to access specific elements of an array - it is important to understand how this works for arrays of varying dimensions. **Important to remember** is that python is zero-indexed i.e. the first position in a list, an array or any other data structure has an index of zero.

## 1-dimensional indexing

Let's start by making a simple array of random numbers:

```python
rand=numpy.random.random(7)
```

The best way to think about slicing an array is to imagine a syntax structure of ```array[start_slice:end_slice:step]``` (where not all of the variables (start_slice, end_slice, step) need to be set).

To get the first value of the array by index, type:

```python
rand[0]
```

To get the first 3 values of the array ```rand``` by index, type:

```python
rand[0:3]
```

To take a slice, accessing all values:

```python
rand[:]
```

To take a slice and get all but the last value:

```python
rand[:-1]
```

To reverse the array:

```python
rand[::-1]
```

To get every second value:

```python
rand[::2]
```

All of the above can be assigned to a variable - it is worth taking notice the type of object that is created according to what is returned by the index/slice:

```python
val=rand[1]
val.dtype
```

returns:

	dtype('float64')

```python
skip=rand[::2]
type(skip) 
```

returns:

	numpy.ndarray

Try using ```numpy.dtype(skip)``` on this second example - why don't you think it works? If you're not sure, check the function documentation.

## 2-dimensional+ indexing

Let's start by making a *2-dimensional* random array:

```python
rand2=numpy.random.random((5,3))
```

Indexing in multiple dimensions is the same as for 1-dimension, except that your slice statements are specified per dimension. Accessing the dimensions of an array can be visualised as:

	1-dimension:  array[1st_dimsnsion]
	2-dimensions: array[1st_dimsnsion,2nd_dimension]
	3-dimensions: array[1st_dimsnsion,2nd_dimension,3rd_dimension]

To access all elements of the 1st dimension (you can imagine this as the top row):

```python
rand2[0,:]
```

To access all elements of the 1st 2 dimensions (you can imagine this as the top 2 rows):

```python
rand2[0:2,:]
```

To access the first element of each dimension (you can imagine this as the 1st column):

```python
rand2[:,0]
```

To access the first 2 elements of each dimension (you can imagine this as the 2 columns):

```python
rand2[:,0:2]
```

# [Previous](../numpy_array_funcs) [Home](../README_numpy) [Next](../numpy_multiplication)
