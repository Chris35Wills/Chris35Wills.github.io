---
---

# Multiplication of arrays

This is a brief note but something that you may find yourself doing a lot when working wih numpy. The great thiing about arrays is that you can quickly multiply and manipulate them without having to specifically loop through each element.

Create 2 2d arrays of random number between zero and 10:

```python
import numpy
random_1=numpy.random.random((5,5))*10
random_2=numpy.random.random((5,5))*10
```

To multiply the elements of random_1 by random_2, you can type (and assign it to its own variable) using:

```python
random_prod=random_1*random_2
```

Now, both ```random_1``` and ```random_2``` are matrices. Using the above operation is a *pair wise* multiplication (e.g. element 1 of random_1 multiplied by element 1 of random_2). To actually carry out a true (mathematical) matrix multiplication you must type:

```python
mtrx_prod=random_1.dot(random_2)
```

Anyway, just so you know and are aware of the difference.

There is a lot of useful information on nummerical operations for arrays available [here](http://www.scipy-lectures.org/intro/numpy/operations.html).

# [Previous](../numpy_indexing) [Home](../README_numpy) [Next](../numpy_io_text)