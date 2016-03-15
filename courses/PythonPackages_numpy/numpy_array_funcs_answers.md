---
---

# Array fucntions: Solutions

# Task 1: Create a *1-dimensional* array of ones and print out its shape

# Solution:

	arr_1d=np.ones(10)
	arr_1d.shape

# Task 2: Create a *2-dimensional* array of random numbers and print out its shape

# Solution:

	rand_2d=numpy.random.random((5,5))
	rand_2d.shape

# Task 3: Create a *2-dimensional* array of values between 10 and 30 and print out its shape

# Solution:

	arr=np.arange(10,30)
	arr_2d=arr.reshape(2,10)
	arr_2d.shape

# Task 4: Create a 10 x 10 *2-dimensional* numpy array of random numbers - what are the max, min and mean values of this array?

# Solution:

	rand_2d=numpy.random.random((5,5))
	print(rand_2d.max())
	print(rand_2d.min())
	print(rand_2d.mean())





